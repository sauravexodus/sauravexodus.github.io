# Monthly Visibility Growth Report — October 2026

Site: https://souravchandra.com

Generated: 2026-11-01 UTC

Period covered: 2026-10-01 through 2026-10-31, with the 2026-11-01 daily rollup used as the latest available trailing-7-day cross-check.

## Executive summary

October kept Search Console collection, technical SEO, and daily measurement healthy while expanding the sitemap from nine to eleven valid routes. The technical-DD companion article from PR #121 and the applied dev-shop-quote article from PR #123 both reached production. All 11/11 sitemap routes now return HTTP 200 with complete tracked metadata, PageSpeed SEO remains 100, and the late-month mobile lab scores rose to 99–100.

Search visibility still did not compound into qualified discovery. The trailing-7-day Search Console snapshot moved from **10 impressions, 0 clicks, and average position 16.3** on 2026-10-01 to **12 impressions, 0 clicks, and average position 7.2** on 2026-10-31. The 2026-11-01 cross-check improved to **17 impressions, 0 clicks, and average position 6.9**, but sampled queries remained Sourav/name-navigation variants and the corrected count stayed at **0 topical non-brand queries**. Five overlapping mid-month snapshots each contained one name-query click; they cannot be summed and may reflect the same underlying click.

The only positive external discovery signal was one bounded DuckDuckGo result set on 2026-10-16 that included Sourav's canonical non-technical-founder guide. It was an ordinary search result, not an AI answer, and it was not repeatably observed later in the month. Across all 109 October prompt rows, no determinate AI-answer response was available, so AI mention and citation rates remain **n/a / blocked**, not 0%.

The critical operational blocker is now queue item 9. PR #123 is merged and production-verified, but `seo/strategy.md` still records Q9 as `DRAFT PR #123 — WAITING HUMAN APPROVAL`. The substantive lane correctly remains `BLOCKED_UNSAFE_STATE` until Sourav interactively confirms the exact frozen candidate and reconciles the release record. Q10 must not be selected before that happens.

## GSC trend and blockers

| Snapshot | Covered period | Status | Trailing-7d impressions | Clicks | CTR | Avg position | Topical non-brand queries | Interpretation |
|---|---|---|---:|---:|---:|---:|---:|---|
| 2026-10-01 | 2026-09-24→2026-09-30 | OK | 10 | 0 | 0.00% | 16.3 | 0 | Name-query discovery only. |
| October low | Rolling snapshots during October | OK | 4 | 1 | 25.00% | 7.8 | 0 | Low-volume branded window; not a topical breakthrough. |
| October high | Rolling snapshots during October | OK | 15 | 0 | 0.00% | 8.7 | 0 | Low-volume fluctuation; overlapping windows must not be summed. |
| 2026-10-31 | 2026-10-24→2026-10-30 | OK | 12 | 0 | 0.00% | 7.2 | 0 | Position improved, but the top query remained a name variant. |
| 2026-11-01 | 2026-10-25→2026-10-31 | OK | 17 | 0 | 0.00% | 6.9 | 0 | Latest cross-check; still no qualified topical discovery. |

- **Property access:** healthy on all 31 October collector runs through the dedicated service account and healthy again on 2026-11-01. Search Console verification/property access is not blocked.
- **Trend:** October snapshots ranged from 4 to 15 trailing-7-day impressions. Five overlapping snapshots from 2026-10-13 through 2026-10-17 each showed one name-query click; they are not five independent monthly clicks.
- **Position caveat:** average position ranged from 7.2 to 17.8 in October and improved to 6.88 in the latest scorecard. Because sampled queries remain name variants, the apparent ranking strength does not prove fractional-CTO, CaaS, AI-MVP, technical-DD, or founder-guide discovery.
- **Real search blocker:** the latest window has 17 impressions, 0 clicks, and 0 corrected topical non-brand queries against 300 impressions, 8 clicks, and 12 non-brand queries in the 30-day benchmark.
- **Manual states:** sitemap submission/request-indexing completion remains unchecked in `seo/strategy.md`. Bing Webmaster ownership and sitemap submission remain unconfirmed in the repository.

## PageSpeed, performance, accessibility, and technical health

| URL | 2026-10-01 mobile perf | 2026-10-31 mobile perf | October successful range | End-of-month LCP / CLS / TBT | SEO | Accessibility |
|---|---:|---:|---:|---|---:|---:|
| `/` | 89 | 100 | 86–100 | 1.5s / 0.004 / 0ms | 100 | 96 |
| `/blog/` | 88 | 99 | 86–100 | 1.5s / 0 / 0ms | 100 | 83 |
| Fractional CTO guide | 87 | 100 | 86–100 | 1.5s / 0 / 0ms | 100 | 85 |
| CaaS guide | 89 | 99 | 80–99 | 1.5s / 0 / 0ms | 100 | 86 |

- **Technical/indexability:** route coverage grew from 9/9 to 11/11 after PRs #121 and #123. Every route remained HTTP 200 with complete tracked title, description, canonical, JSON-LD, and indexability checks.
- **Performance:** all four tracked URLs had successful scored samples on every October day. Scores were generally in the high 80s until a broad 2026-10-30 shift to 99–100 with LCP dropping from roughly 3.0s to 1.5s; the 2026-11-01 sample retained those values.
- **Attribution caveat:** no October performance PR explains the simultaneous lab-score change across every monitored route. Treat it as an encouraging PageSpeed measurement shift and confirm persistence rather than claiming a shipped optimization caused it.
- **SEO:** 100 on every successful monitored sample.
- **Accessibility:** unchanged and still the clearest UX deficit. `/blog/` remains the floor at 83 against the target of 95; the tracked articles remain 85–86.

## Benchmark target status

Latest scorecard snapshot: 2026-11-01.

| Metric | Current | Target | Status | Interpretation |
|---|---:|---:|---|---|
| Google impressions / trailing 7d | 17 | 300 | Behind | 283 below target; no topical query yet. |
| Google clicks / trailing 7d | 0 | 8 | Behind | No qualified organic traffic in the latest window. |
| CTR | 0.0% | 1.5% | Behind | Qualified discovery is too low for snippet improvements to compound. |
| Avg position | 6.88 | 50 or better | Stretch | Misleading positive because sampled rows are name-navigation queries. |
| Non-brand queries with impressions | 0 | 12 | Behind | Primary growth gap. |
| Live sitemap routes HTTP 200 | 100% (11/11) | 100% | Stretch | Protect. |
| Metadata coverage | 100% (11/11) | 100% | Stretch | Protect. |
| Homepage mobile PageSpeed | 100 | 90 | Stretch | Confirm the late-month shift persists. |
| PageSpeed SEO | 100 | 100 | Stretch | Protect. |
| Minimum accessibility | 83 | 95 | Watch | `/blog/` remains the floor. |
| AI/GEO mention rate | n/a | 5% | Blocked | Newest 40 rows contain no determinate AI-answer result. |
| AI/GEO citation rate | n/a | 2% | Blocked | Newest 40 rows contain no determinate AI-answer result. |
| SERP top-20 coverage | n/a | 5% | Blocked | Dedicated reproducible rank metric is not populated. |
| SERP top-10 coverage | n/a | 6% at 90d | Blocked | Dedicated reproducible rank metric is not populated. |
| Source-gap closure | n/a | 3 | Blocked | Action tracker does not yet populate the metric. |

Status distribution: **5 Stretch, 1 Watch, 4 Behind, and 5 Blocked**. Technical safeguards and the latest homepage lab score meet target; discovery, authority, accessibility, and measurement completeness do not.

## AI/GEO mention and citation trend

- **October volume:** 109 prompt rows across 20 weekday research dates.
- **Bounded search evidence:** 22 usable ordinary-search result sets contained no Sourav/domain match.
- **Positive search evidence:** one 2026-10-16 DuckDuckGo set included Sourav's canonical founder guide. This is a search-visible mention/link, not a determinate AI-answer mention or citation.
- **Excluded evidence:** 86 rows were indeterminate because surfaces were challenged, throttled, empty, mixed, unrelated, intent-drifted, or non-extractable.
- **Direct AI-answer denominator:** 0 determinate rows. AI-answer mention and citation rates therefore remain **n/a / blocked**.
- **Month-over-month:** September had 53 bounded search negatives and 61 indeterminate rows with no positive. October produced one positive bounded search set, but usable evidence fell to 23 of 109 rows and the positive did not establish durable discovery or any AI-answer trend.
- **Measurement rule:** direct competitor/source fetches support research only. They do not establish prompt presence, exact rank, demand, source independence, indexation, or AI citation.

## Competitor and trend findings

1. **Provider-led service surfaces persist:** fractional-CTO, CaaS, proposal, agency-versus-in-house, and handover sets remain dominated by providers, practitioners, directories, repeated forum threads, and videos. Sourav's strongest differentiation remains independent buyer-side judgment and acceptance evidence, not another provider list or interchangeable location page.
2. **Canonical consolidation remains correct:** the existing fractional-CTO, CaaS, AI-MVP/RAG, technical-DD, and founder pairs already cover the durable buyer decisions. October evidence repeatedly ended as `REPEAT_CONFIRMATION`; annual, pricing, SLA, checklist, handover, rollback, and city variants would split authority without first-party demand or distinct information gain.
3. **Evidence-to-decision is the technical-DD edge:** current sources converge on dated evidence, finding, uncertainty, business or thesis impact, remediation owner/timing, decision gate, and closure evidence. The checklist plus PR #121's codebase companion are the correct two canonicals.
4. **Demonstrated control is the founder/agency edge:** quote and handover research converges on objective acceptance, buyer-owned repositories and accounts, reproducible setup, deployment/recovery, credential control, written sign-off, and successor independence. Keep this inside the broad founder guide and PR #123's applied quote article.
5. **AI guidance needs lifecycle maintenance, not another generic guide:** OpenAI's Evals transition, fine-tuned-model shutdown dates, and 12-hour prompt-cache option are implementation constraints. Durable public advice should remain provider-independent and pair representative evaluations with human authority, staged release, monitoring, rollback, retrieval diagnosis, and workload-level economics.
6. **Q11 remains viable but monitor-only:** the future fractional-CTO board memo has a bounded decision/risk/runway/owner/next-action shape, but it must wait behind Q9 reconciliation and Q10 rotation.
7. **Source decay is material:** October checks found timeouts, DNS failures, certificate failures, generic redirects, empty shells, outdated routes, and provider pages that disappeared. Every approved claim needs a fresh final-domain, title, lifecycle, relevance, and exact-support check.

## Actions shipped and PRs merged

**46 pull requests merged in October (#100–#145), plus 31 daily collector commits on `master`.** GitHub Pages deploys from `master`; the recurring action ledger records matching Pages runs and canonical-domain marker verification for the research and release-record PRs.

### Public/editorial state

- **#119 and #120 — Q5 release reconciliation:** recorded Sourav's interactive ratification of the exact prior candidate and restored the substantive lane before the next editorial selection.
- **#121 — technical-DD companion:** published `/blog/how-vcs-evaluate-a-codebase.html`; **#122** reconciled its approved release state.
- **#123 — dev-shop quote article:** published `/blog/how-to-evaluate-a-dev-shop-quote.html` and expanded the sitemap to 11 routes. Source, Pages deployment, and production markers are verified, but the checked-in queue still says Q9 is waiting for human approval. This report does not infer approval from the owner merge.

### Measurement, research, and governance

- **40 report-only visibility research/release PRs:** #101–#118 and #124–#145 covered 20 weekday passes and their durable release/status records.
- **#100 — reporting:** published the September visibility growth report.
- Daily collection produced one authoritative raw row for every October date, with authenticated GSC, route/metadata, PageSpeed, and benchmark updates and no duplicate October raw dates.
- Research improved evidence-state discipline, source-lifecycle checks, canonical consolidation, and release-state reporting without auto-publishing another near-duplicate public page.

## Next priorities for November

1. **Reconcile PR #123 interactively:** confirm the exact intended Q9 approval/release record. Until then, keep Q9 `WAITING_HUMAN`, the substantive lane `BLOCKED_UNSAFE_STATE`, and Q10 unselected.
2. **Create topical discovery:** monitor GSC for the two October routes and established service/topic canonicals. Treat name-query position as navigation, not commercial progress; use first-party topical query evidence before changing titles, anchors, or route inventory.
3. **Confirm webmaster states:** GSC property access works, so do not request new OAuth. Confirm or submit `https://souravchandra.com/sitemap.xml`, record request-indexing state where applicable, and verify Bing Webmaster ownership plus sitemap submission.
4. **Restore direct AI-answer measurement:** obtain determinate answer-engine evidence or keep mention/citation metrics at `n/a`; never turn ordinary SERP absence into a 0% AI-answer rate.
5. **Complete benchmark instrumentation:** populate reproducible SERP top-20/top-10 coverage and source-gap closure.
6. **Raise the accessibility floor:** prioritize `/blog/` at 83, followed by article templates at 85–86, toward the 95 target.
7. **Confirm performance persistence:** continue monitoring the late-October 99–100 scores and 1.5s LCP before treating the change as durable.
8. **Maintain source lifecycle and consolidation:** recheck dated OpenAI/NIST/CISA/provider sources before approved edits; reject thin annual, regional, pricing, checklist, evaluation, or handover variants without distinct buyer intent, evidence, preview, and named approval.

## Blockers to report

- **Search Console verification/property access is not blocked.** Service-account collection for `sc-domain:souravchandra.com` succeeded on all 31 October runs and on 2026-11-01.
- **Topical search discovery remains blocked in practice:** 17 impressions, 0 clicks, and 0 corrected topical non-brand queries in the latest trailing-seven-day window.
- **Sitemap submission/request-indexing and Bing Webmaster status remain unconfirmed** in the repository.
- **Direct AI-answer visibility is unmeasured:** the scorecard correctly reports mention and citation as `n/a / blocked`, not 0%.
- **SERP coverage and source-gap closure metrics remain unimplemented/blocked.**
- **Accessibility remains below target**, especially `/blog/` at 83.
- **Editorial state is unsafe:** PR #123 is merged/live while Q9 remains `WAITING HUMAN APPROVAL`; substantive automation must remain blocked pending interactive reconciliation.
