import tempfile
import unittest
from pathlib import Path

from scripts import score_visibility_benchmarks as scorer


HEADER = """# AI / GEO Visibility Weekly

| Date UTC | Weekday Theme | Prompt / Query | Sourav Mentioned | souravchandra.com Cited | Observed Sources / Competitors | Evidence | Action |
|---|---|---|---|---|---|---|---|
"""


def row(date: str, mention: str, citation: str) -> str:
    return (
        f"| {date} | Theme | Prompt | {mention} | {citation} | Sources | "
        "Evidence | Action |"
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
            "Scored 40 determinate rows; 0 indeterminate excluded from newest 40 rows",
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
            "Scored 2 determinate rows; 1 indeterminate excluded from newest 3 rows",
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


if __name__ == "__main__":
    unittest.main()
