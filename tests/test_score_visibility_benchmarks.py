import tempfile
import unittest
import json
from pathlib import Path

from scripts import collect_visibility_metrics as collector
from scripts import score_visibility_benchmarks as scorer


HEADER = """# AI / GEO Visibility Weekly

| Date UTC | Weekday Theme | Prompt / Query | Sourav Mentioned | souravchandra.com Cited | Observed Sources / Competitors | Evidence | Action |
|---|---|---|---|---|---|---|---|
"""


def row(date: str, mention: str, citation: str, evidence: str = "Evidence") -> str:
    return (
        f"| {date} | Theme | Prompt | {mention} | {citation} | Sources | "
        f"{evidence} | Action |"
    )


class AiRatesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.original_report_dir = scorer.REPORT_DIR
        scorer.REPORT_DIR = Path(self.tempdir.name)

    def tearDown(self) -> None:
        scorer.REPORT_DIR = self.original_report_dir
        self.tempdir.cleanup()

    def write_rows(self, rows: list[str]) -> None:
        (scorer.REPORT_DIR / "ai-visibility-weekly.md").write_text(
            HEADER + "\n".join(rows) + "\n",
            encoding="utf-8",
        )

    def test_ai_rates_use_the_newest_rows_from_newest_first_report(self) -> None:
        rows = [row("2026-08-10", "Yes", "Yes")]
        rows.extend(row("2026-08-09", "No", "No") for _ in range(40))
        self.write_rows(rows)

        mention_rate, citation_rate, note = scorer.ai_rates()

        self.assertEqual(mention_rate, 2.5)
        self.assertEqual(citation_rate, 2.5)
        self.assertEqual(
            note,
            "Scored 40 AI-answer rows; 0 non-AI-answer/indeterminate excluded from newest 40 rows",
        )

    def test_ai_rates_exclude_indeterminate_rows_and_report_denominator(self) -> None:
        self.write_rows(
            [
                row("2026-08-10", "Indeterminate / not scored", "Indeterminate / not scored"),
                row("2026-08-09", "Yes", "Yes"),
                row("2026-08-08", "No", "No"),
            ]
        )

        mention_rate, citation_rate, note = scorer.ai_rates()

        self.assertEqual(mention_rate, 50.0)
        self.assertEqual(citation_rate, 50.0)
        self.assertEqual(
            note,
            "Scored 2 AI-answer rows; 1 non-AI-answer/indeterminate excluded from newest 3 rows",
        )

    def test_ai_rates_exclude_search_visible_rows(self) -> None:
        self.write_rows(
            [
                row(
                    "2026-08-10",
                    "No in usable result set",
                    "No in usable result set",
                    "Bounded search-visible evidence, not an AI-answer result.",
                ),
                row("2026-08-09", "Yes", "Yes", "Verified AI-answer response."),
            ]
        )

        mention_rate, citation_rate, note = scorer.ai_rates()

        self.assertEqual(mention_rate, 100.0)
        self.assertEqual(citation_rate, 100.0)
        self.assertEqual(
            note,
            "Scored 1 AI-answer rows; 1 non-AI-answer/indeterminate excluded from newest 2 rows",
        )

    def test_ai_rates_do_not_skip_data_rows_containing_header_words(self) -> None:
        dated_row = row("2026-09-03", "No", "No").replace(
            "Evidence", "Dated Weekly evidence"
        )
        self.write_rows([dated_row])

        mention_rate, citation_rate, note = scorer.ai_rates()

        self.assertEqual(mention_rate, 0.0)
        self.assertEqual(citation_rate, 0.0)
        self.assertEqual(
            note,
            "Scored 1 AI-answer rows; 0 non-AI-answer/indeterminate excluded from newest 1 rows",
        )

    def test_ai_rates_do_not_skip_data_rows_containing_separator_text(self) -> None:
        separator_text_row = row("2026-09-03", "No", "No").replace(
            "Evidence", "A---B evidence boundary"
        )
        self.write_rows([separator_text_row])

        mention_rate, citation_rate, note = scorer.ai_rates()

        self.assertEqual(mention_rate, 0.0)
        self.assertEqual(citation_rate, 0.0)
        self.assertEqual(
            note,
            "Scored 1 AI-answer rows; 0 non-AI-answer/indeterminate excluded from newest 1 rows",
        )


class CurrentMetricsTests(unittest.TestCase):
    def test_missing_home_pagespeed_does_not_use_another_route(self) -> None:
        rec = {
            "gsc": {"status": "BLOCKED_AUTH"},
            "routes": {"total": 2, "ok": 2, "metadata_ok": 2},
            "pagespeed": [
                {
                    "url": scorer.BASE + "/",
                    "status": "SYNTHETIC",
                    "pagespeed_status": "ERROR",
                    "performance": None,
                },
                {
                    "url": scorer.BASE + "/blog/",
                    "status": "OK",
                    "performance": 89,
                    "seo": 100,
                    "accessibility": 83,
                },
            ],
        }

        metrics = scorer.current(rec)

        self.assertEqual(
            metrics["pagespeed_mobile_home"],
            (None, "", "ERROR+SYNTHETIC"),
        )
        self.assertEqual(metrics["pagespeed_seo"], (100.0, "", "Minimum across tracked URLs"))
        self.assertEqual(metrics["pagespeed_accessibility"], (83.0, "", "Minimum across tracked URLs"))


class PreviousGscBlockerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.original_report_dir = collector.REPORT_DIR
        self.original_raw_dir = collector.RAW_DIR
        collector.REPORT_DIR = Path(self.tempdir.name) / "reports"
        collector.RAW_DIR = collector.REPORT_DIR / "raw"
        collector.RAW_DIR.mkdir(parents=True)

    def tearDown(self) -> None:
        collector.REPORT_DIR = self.original_report_dir
        collector.RAW_DIR = self.original_raw_dir
        self.tempdir.cleanup()

    def write_raw_statuses(self, *statuses: str) -> None:
        rows = [json.dumps({"date": f"2026-09-{index:02d}", "gsc": {"status": status}})
                for index, status in enumerate(statuses, start=1)]
        (collector.RAW_DIR / "visibility-metrics.jsonl").write_text(
            "\n".join(rows) + "\n", encoding="utf-8"
        )

    def test_recent_ok_clears_an_older_site_access_blocker(self) -> None:
        self.write_raw_statuses("BLOCKED_SITE_ACCESS", "OK")
        (collector.REPORT_DIR / "search-visibility-daily.md").write_text(
            "| 2026-09-01 | BLOCKED_SITE_ACCESS |\n", encoding="utf-8"
        )

        self.assertIsNone(collector.previous_gsc_blocker())

    def test_recent_site_access_blocker_survives_a_later_auth_gap(self) -> None:
        self.write_raw_statuses("OK", "BLOCKED_SITE_ACCESS")

        self.assertEqual(
            collector.previous_gsc_blocker(),
            "BLOCKED_SITE_ACCESS",
        )

    def test_newer_markdown_ok_clears_an_older_raw_blocker(self) -> None:
        self.write_raw_statuses("BLOCKED_SITE_ACCESS")
        (collector.REPORT_DIR / "search-visibility-daily.md").write_text(
            "| 2026-09-02 | OK |\n", encoding="utf-8"
        )

        self.assertIsNone(collector.previous_gsc_blocker())

    def test_newer_raw_blocker_overrides_an_older_markdown_ok(self) -> None:
        self.write_raw_statuses("OK", "BLOCKED_SITE_ACCESS")
        (collector.REPORT_DIR / "search-visibility-daily.md").write_text(
            "| 2026-09-01 | OK |\n", encoding="utf-8"
        )

        self.assertEqual(
            collector.previous_gsc_blocker(),
            "BLOCKED_SITE_ACCESS",
        )


if __name__ == "__main__":
    unittest.main()
