# Monthly Visibility Growth Report — August 2026

Site: https://souravchandra.com

Generated: 2026-09-01 UTC

Period covered: 2026-08-01 through 2026-08-31, with the 2026-09-01 daily rollup used as the latest available trailing-7-day cross-check.

## Executive summary

August preserved a healthy technical SEO/GEO base and shipped four source-backed improvements to existing strategic articles. Search Console collection is working through the `sc-domain:souravchandra.com` property and the service account, all seven sitemap routes and metadata checks remain healthy, and tracked PageSpeed SEO remains 100.

Visibility did not compound. The trailing-7-day GSC snapshot moved from **18 impressions, 0 clicks, and average position 7.2** on 2026-08-01 to **11 impressions, 0 clicks, and average position 14.5** on 2026-08-31. The 2026-09-01 cross-check is **12 impressions, 0 clicks, and average position 13.8**. A single click appeared in the 2026-08-20 through 2026-08-25 rolling windows, but it came from a Sourav-name query. Corrected query classification found **0 topical non-brand queries** throughout the rest of the month.

AI/GEO visibility also remained at zero. August recorded 102 tracked prompt checks: 50 determinate result sets contained no Sourav/domain mention or citation, while 52 challenged, throttled, noisy, or intent-drifted checks were correctly excluded. The latest 40-row scorecard window deteriorated to only 12 determinate rows and 28 excluded rows, so measurement availability is also a constraint.

## GSC trend and blockers

| Snapshot | Covered period | Status | Trailing-7d impressions | Clicks | CTR | Avg position | Topical non-brand queries | Interpretation |
|---|---|---|---:|---:|---:|---:|---:|---|
| 2026-08-01 | 2026-07-25→2026-07-31 | OK | 18 | 0 | 0.00% | 7.2 | Historical row showed 1 | Pre-fix classifier still counted a person-name variant; not commercial discovery. |
| 2026-08-20 | 2026-08-13→2026-08-19 | OK | 14 | 1 | 7.14% | 21.7 | 0 | First recorded click was from `sourav chandra`; homepage/name-query behavior only. |
| 2026-08-25 | 2026-08-18→2026-08-24 | OK | 10 | 1 | 10.00% | 14.5 | 0 | Same person-name click remained in the rolling window. |
| 2026-08-31 | 2026-08-24→2026-08-30 | OK | 11 | 0 | 0.00% | 14.5 | 0 | No topical discovery; sampled queries still point to `/`. |
| 2026-09-01 | 2026-08-25→2026-08-31 | OK | 12 | 0 | 0.00% | 13.8 | 0 | Latest cross-check; still name-query only. |

**Search Console blocker status:** there is **no current Search Console OAuth, property-access, or verification blocker**. Daily automation is successfully querying `sc-domain:souravchandra.com` with the service account. The unchecked manual GSC item in `seo/strategy.md` is stale relative to the live collector evidence. Sitemap submission/request-indexing completion is not recorded, and Bing Webmaster ownership/sitemap status is repeatedly marked “if still pending,” so those manual states still need confirmation.

The real search blocker is topical discovery: rolling impressions are low, the homepage is the only sampled top page, and the corrected data has no fractional-CTO, CaaS, AI-MVP, technical-DD, or founder-guide query.

## PageSpeed, performance, accessibility, and technical health

| URL | 2026-08-01 mobile perf | 2026-08-31 mobile perf | August range | LCP / CLS / TBT pattern | SEO | Accessibility |
|---|---:|---:|---:|---|---:|---:|
| `/` | 89 | 89 | 88–89 across successful samples | About 3.0s / 0.003–0.004 / 0ms | 100 | 96 |
| `/blog/` | 89 | 89 | 86–89 | About 3.0–3.1s / 0–0.017 / 0ms | 100 | 83 |
| Fractional CTO guide | 89 | 86 | 86–93 | About 2.6–3.1s / 0–0.001 / 0ms | 100 | 85 |
| CaaS guide | 89 | 88 | 86–89 | About 3.0–3.1s / 0–0.001 / 0ms | 100 | 86 |

- **Technical/indexability:** 7/7 sitemap routes returned HTTP 200 and 7/7 had complete tracked metadata throughout the month.
- **Performance:** stable but below the homepage target of 90; the latest 2026-09-01 homepage score is 88.
- **Reliability:** homepage PageSpeed returned API/Lighthouse errors on 2026-08-21 and 2026-08-26. The scorer now correctly marks the exact homepage sample blocked instead of borrowing another route's score; subsequent samples recovered.
- **Accessibility:** unchanged and still the main UX deficit. `/blog/` remains 83, below the 95 target; tracked articles remain 85–86.
- **Raw-data note:** the JSONL archive retains five 2026-08-02 auth-repair transition samples (`BLOCKED_SITE_ACCESS`, `BLOCKED_AUTH`, and three `OK` samples). For each date, the authoritative sample is the **last appended `OK` row with `gsc.tokenSource: service-account`**; earlier transition and duplicate rows are excluded. Raw-row aggregations must preserve append order rather than deduplicating only by date or status.

## Benchmark target status

Latest scorecard snapshot: 2026-09-01.

| Metric | Current | 30-day target | Status | Interpretation |
|---|---:|---:|---|---|
| Google impressions / trailing 7d | 12 | 300 | Behind | 4% of target; no topical query yet. |
| Google clicks / trailing 7d | 0 | 8 | Behind | The mid-month name-query click has left the rolling window. |
| CTR | 0.0% | 1.5% | Behind | Too little qualified discovery to optimize meaningfully. |
| Avg position | 13.83 | 50 or better | Stretch | Misleading positive: sampled rows are name/person queries, not target topics. |
| Non-brand queries with impressions | 0 | 12 | Behind | Primary growth gap. |
| Live sitemap routes HTTP 200 | 100% | 100% | Stretch | Protect. |
| Metadata coverage | 100% | 100% | Stretch | Protect. |
| Homepage mobile PageSpeed | 88 | 90 | Watch | Two points below target. |
| PageSpeed SEO | 100 | 100 | Stretch | Protect. |
| Minimum accessibility | 83 | 95 | Watch | `/blog/` remains the floor. |
| AI/GEO mention rate | 0.0% | 5% | Behind | Latest 40 rows: 12 determinate, 28 excluded. |
| AI/GEO citation rate | 0.0% | 2% | Behind | No verified domain citation. |
| SERP top-20 coverage | n/a | 5% | Blocked | Dedicated rank/source data is not implemented. |
| Source-gap closure | n/a | 3 | Blocked | Four source-backed page improvements shipped, but this metric is not populated. |

Interpretation: technical targets are protected, while every meaningful discovery/authority target remains behind. The `source_gap_closure` and SERP coverage rows need measurement implementation before they can be used as decision signals.

## AI/GEO mention and citation trend

- **August total:** 102 prompt rows across 20 research dates; 50 determinate and 52 indeterminate/excluded.
- **Verified outcome:** 0 Sourav mentions and 0 `souravchandra.com` citations in all 50 usable result sets.
- **Latest scorecard window:** 12 determinate and 28 indeterminate rows out of the newest 40, with 0% mention and citation rates.
- **Measurement trend:** result availability worsened late in the month. The 2026-08-31 pass had 0/5 determinate prompts because DuckDuckGo challenged, Brave throttled, Bing lost intent, and Google's fallback was non-extractable.
- **Interpretation boundary:** most evidence is bounded search-visible fallback data, not direct AI-answer coverage. It can establish a clean visible-set absence when usable, but cannot support exact rank, full-SERP coverage, or AI-answer claims.

## Competitor and trend findings

1. **Fractional CTO / CaaS Dubai-UAE:** exact-location provider and practitioner pages remain crowded. Competitors increasingly package scope, named decision rights, first-period audit/risk/roadmap outputs, operating/reporting cadence, notice, handover, and full-time transition. The information-gain opportunity is a buyer acceptance/quote-normalization artifact on the maintained canonical pages, not more Dubai/Abu Dhabi/annual URLs.
2. **AI MVP / RAG vs fine-tuning:** exact-year provider guides, launch checklists, cost pages, and decision matrices proliferated. Primary evidence still supports task-specific objectives, representative eval data, baseline comparisons, human judgment, cost/latency limits, monitoring, and a measured stable-behavior failure before fine-tuning. Queue item 7 remains the strongest next draft if it becomes a founder operating model rather than another definitions matrix.
3. **Technical due diligence:** count-signalled checklists and evidence-pack pages remain visible, while more specific thesis/deal-treatment prompts often lose intent. The differentiated artifact is two-layered: auditable evidence first, then `finding → thesis delta → confidence → decision gate → owner → closure evidence`.
4. **Founder / development agency:** exact-year checklists and proposal-evaluation pages are crowded. The sharper opportunity is a quote-to-handover traceability ledger with founder-owned accounts and a clean-room setup/test/non-production-deploy/core-flow/credential-rotation/rollback-or-restore gate.
5. **Consolidation is a growth strategy:** repeated research showed that near-duplicate location, annual, checklist, handover, provenance, SLA, and evaluation routes would split authority without first-party demand. August correctly kept substantive review-only artifacts out of production after the initial source-backed page improvements.

## Actions shipped and PRs merged

**42 pull requests merged in August (#11–#52).** GitHub Pages deploys from `master`; the recurring action ledger records matching Pages runs and canonical-domain marker verification for the weekday research/release PRs.

### Public article and measurement improvements

- **#12 — CaaS pricing evidence:** added a dated, directly sourced market cross-check without changing Sourav's own rate promise; refreshed sitemap metadata; fixed the non-brand classifier so name variants no longer count as topical discovery.
- **#14 — RAG evaluation guidance:** added source-backed retrieval-versus-generation evaluation guidance, matching FAQ schema, and primary-source links to the AI-MVP article.
- **#16 — AI-generated-code diligence:** added five investor-requestable evidence packets and matching FAQ/source support to the technical-DD article.
- **#18 — AI-assisted agency guidance:** added an AI-use/provenance schedule and matching FAQ/source support to the non-technical-founder article.
- **#21 — AI benchmark integrity:** changed the scorer to exclude indeterminate prompt rows and use the newest 40-row window; added regression tests.
- **#39 — PageSpeed score integrity:** bound homepage performance to the exact homepage row and added a failed-homepage regression test.

### Reporting and release records

- **36 report/release PRs:** #11, #13, #15, #17, #19–#20, #22–#38, and #40–#52.
- Twenty weekday research passes were recorded. Four early passes shipped bounded source-backed improvements to existing pages; later passes preserved existing canonicals, refined review-only briefs, or fixed measurement logic rather than auto-publishing near-duplicate public content.
- No new public route was added in August.

## Next priorities for September

1. **Create first topical discovery:** keep monitoring GSC for fractional CTO, CaaS, AI MVP, RAG/fine-tuning, technical-DD, and founder/agency queries. Do not treat name-query average position as commercial progress.
2. **Confirm manual webmaster states:** GSC API/property access is working, so do not ask for new OAuth. Confirm sitemap submission/request-indexing status, reconcile the stale GSC checkbox in `seo/strategy.md`, and verify Bing Webmaster ownership plus sitemap submission.
3. **Prepare queue item 7 for preview and named approval:** make the RAG-vs-fine-tuning page a founder operating decision model with source boundaries, evaluation readiness, build versus recurring cost, latency, and a revisit trigger. Do not auto-publish substantive copy.
4. **Raise the accessibility floor:** fix `/blog/` from 83 toward 95+, then address the article pages at 85–86.
5. **Nudge mobile performance:** target the homepage and strategic pages toward 90+ and LCP below the current roughly 3.0s pattern; preserve exact-URL PageSpeed failure handling.
6. **Complete benchmark instrumentation:** populate SERP top-20/top-10 coverage and source-gap closure rather than leaving them `n/a`.
7. **Keep canonical consolidation:** do not add Dubai, Abu Dhabi, annual, checklist, SLA, handover, evaluation, or provenance variants without distinct buyer intent, proof, first-party demand, preview, and named approval.

## Blockers to report

- **Search Console verification is not blocked.** Service-account collection for `sc-domain:souravchandra.com` is healthy.
- **Topical search discovery is blocked in practice:** 0 corrected non-brand queries and only 12 latest trailing-7-day impressions.
- **Bing Webmaster and sitemap submission status is unconfirmed** in the repository.
- **AI/GEO authority remains at 0% mention/citation**, and late-month prompt measurement is heavily challenged/throttled.
- **Accessibility remains below target**, especially `/blog/` at 83.
- **SERP coverage and source-gap benchmark metrics remain unimplemented/blocked.**
