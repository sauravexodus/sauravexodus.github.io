# Monthly Visibility Growth Report — July 2026

Site: https://souravchandra.com  
Generated: 2026-08-01 UTC  
Period covered: July 2026 relaunch through 2026-07-31, with the 2026-08-01 daily rollup used as the latest available trailing-7-day snapshot.

## Executive summary

July established the technical SEO/GEO foundation and the recurring measurement loop for souravchandra.com. The site now has sitemap/robots/llms assets, structured metadata coverage, blog routing, interlinked posts, benchmark scorecards, PageSpeed tracking, AI/GEO tracking, competitor/source tracking, industry trend tracking, and safe recurring action logs.

The main visibility signal improved from an early Search Console access blocker to usable `sc-domain:souravchandra.com` data by 2026-07-29. However, discovery is still very early: the latest trailing-7-day sample shows **18 impressions, 0 clicks, 0.00% CTR, average position 7.2**, and the visible queries are still almost entirely branded or misspelled name searches rather than commercial non-brand topics.

## GSC trend and blockers

| Date | Status | Trailing-7d impressions | Clicks | CTR | Avg position | Notes |
|---|---|---:|---:|---:|---:|---|
| 2026-07-26 | BLOCKED_SITE_ACCESS | n/a | n/a | n/a | n/a | Search Console returned insufficient site permission. |
| 2026-07-27 | BLOCKED_SITE_ACCESS | n/a | n/a | n/a | n/a | Site/property access still blocked. |
| 2026-07-28 | BLOCKED_SITE_ACCESS | n/a | n/a | n/a | n/a | Cron preserved the known site-access blocker across auth gaps. |
| 2026-07-29 | OK | 15 | 0 | 0.00% | 9.9 | First usable GSC domain-property sample. |
| 2026-07-30 | OK | 20 | 0 | 0.00% | 9.3 | Still mostly branded/misspelled discovery. |
| 2026-07-31 | OK | 22 | 0 | 0.00% | 9.2 | Non-brand query count still 2 vs 30-day target of 12. |
| 2026-08-01 | OK | 18 | 0 | 0.00% | 7.2 | Top query `saurav chandra`; top page `/`. |

**Blocker status:** GSC data is now reachable from the automation, but the strategy checklist still needs manual Search Console and Bing Webmaster completion: verify/confirm the property, submit `https://souravchandra.com/sitemap.xml`, and request indexing for all current URLs. This remains the highest-leverage manual action because the current impressions are not yet commercial-topic discovery.

## PageSpeed, performance, accessibility, and technical health

- Live route/indexability guard stayed healthy: **7/7 sitemap routes returned HTTP 200** and **7/7 tracked routes had title/meta/canonical/JSON-LD/no noindex** in the benchmark rows.
- SEO score stayed at **100** across tracked PageSpeed URLs.
- Mobile performance stayed stable but just below the 30-day target: homepage was usually **88–89** vs target **90**; latest tracked homepage value is **89**.
- LCP stayed around **3.0s**, CLS near **0**, and TBT **0ms** on tracked PageSpeed rows.
- Accessibility is the main UX weakness: homepage is **96**, but `/blog/` remains **83**, with tracked article pages around **85–86**. Benchmark minimum accessibility remains **83 vs target 95**.

## Benchmark target status

Latest benchmark snapshot (2026-08-01):

| Metric | Current | Target | Status |
|---|---:|---:|---|
| Google impressions / trailing 7d | 18 | 300 | Behind |
| Google clicks / trailing 7d | 0 | 8 | Behind |
| CTR | 0.0% | 1.5% | Behind |
| Avg position | 7.17 | 50 or better | Stretch |
| Non-brand queries with impressions | 1 | 12 | Behind |
| Live sitemap routes HTTP 200 | 100% | 100% | Stretch |
| Metadata coverage | 100% | 100% | Stretch |
| Homepage mobile PageSpeed | 89 | 90 | Watch |
| PageSpeed SEO | 100 | 100 | Stretch |
| Minimum accessibility | 83 | 95 | Watch/Behind |
| AI/GEO mention rate | 0.0% | 5% | Behind |
| AI/GEO citation rate | 0.0% | 2% | Behind |
| SERP top-20 coverage | n/a | 5% | Blocked / not yet reliably measured |

Interpretation: technical SEO is healthy; visibility, clicks, non-brand query breadth, AI/GEO mentions, and accessibility are behind target.

## AI/GEO mention and citation trend

- AI/GEO tracking rows across fractional CTO UAE/Dubai, CTO-as-a-service Dubai/pricing, AI MVP/RAG/fine-tuning, technical due diligence, and non-technical founder/dev-agency prompts all show **0 verified Sourav mentions and 0 souravchandra.com citations**.
- The robots/llms foundation improved in July: root `llms.txt` was added, and `robots.txt` explicitly allows additional search/AI crawlers including Perplexity-User, Applebot-Extended, and Bingbot.
- Current AI/GEO gap is not metadata. It is authority/source visibility: AI answers still cite competitors and high-authority sources because souravchandra.com is only beginning to appear in Google data and has not yet earned non-brand citation visibility.

## Competitor and trend findings

Key July findings from tracking reports:

1. **Fractional CTO Dubai/UAE:** agency and practitioner/location pages dominate. Competitors include fractional-dubai.com, hirefractional.io, digitalreference.co, golosnichenko.com, boardman.com, SAIA Digital, Fusion AI, Alex Kadyrov, Kompella, and Solokit. The recurring pattern is exact location/pricing pages, full-time-vs-fractional cost comparisons, and UAE/DIFC/compliance framing.
2. **CTO-as-a-service Dubai/pricing:** pages with concrete price bands and packaged diagnostics are visible. Sourav's AED 15k–40k retainer framing and full-time CTO comparison are directionally aligned; a future scannable pricing-model comparison could help after indexing improves.
3. **AI MVP/RAG/fine-tuning:** generic RAG/fine-tuning definitions are owned by IBM, Pinecone, Databricks, and similar authoritative sources. Sourav's opportunity is a founder-stage decision guide with cost, eval readiness, freshness, lock-in, latency, and month-six revisit logic, not another glossary.
4. **Technical due diligence:** SERPs reward count signals and investor framing: 25 documents, 54 items, seven areas/domains. The differentiated angle is not a longer checklist; it is translating checklist findings into investor/pricing decisions and AI-code supervision risks.
5. **Founder/dev-agency:** broad hiring and outsourcing SERPs are noisy. The best gap is narrower: line-item dev-shop quote due diligence for non-technical founders before signing.

## Actions shipped / PRs merged

July PRs merged:

- #1 — `feat: add visibility growth benchmarking`: added daily visibility metrics, benchmark scorecard, expected outcomes, and recurring measurement foundation.
- #2 — `chore: add GEO visibility reports and llms.txt`: added AI/GEO reports, `llms.txt`, and expanded crawler allowlist.
- #3 — `docs: update visibility PR status`: kept recurring-action report state current.
- #4 — `chore: record CaaS pricing visibility scan`: recorded CTO-as-a-service/pricing scan and related report updates.
- #5 — `chore: record Wednesday AI visibility loop`: added AI/RAG/fine-tuning visibility intelligence and fixed GSC blocker preservation behavior.
- #6 — `chore: mark visibility PR merged`: status/report housekeeping.
- #7 — `fix: use ADC quota project for Sourav GSC metrics`: fixed authenticated GSC metrics access via ADC quota project.
- #8 — `chore: update technical DD visibility loop`: updated technical-DD visibility intelligence and strengthened the DD page with the seven-decision/checklist differentiation.
- #9 — `chore: mark visibility PR merged`: status/report housekeeping.
- #10 — `Improve founder guide quote review SEO`: strengthened the founder guide with quote-review content, FAQPage JSON-LD, and report updates.

Additional shipped site/content work visible in git history includes the July relaunch SEO/GEO foundation, blog setup, AI MVP post, technical-DD post, founder-guide post, CTO-as-a-service Dubai post, interlinking fixes, sitemap updates, and daily visibility metric commits.

## Next priorities for August

1. **Manual indexing unblock:** confirm GSC property access, submit `https://souravchandra.com/sitemap.xml`, request indexing for `/`, `/blog/`, and all blog URLs; also verify Bing Webmaster Tools because Bing powers important answer/search surfaces.
2. **Publish the next AI-cluster page:** `RAG vs fine-tuning: what your startup actually needs (and what each costs)`, with a decision table and internal links from the AI MVP page.
3. **Improve accessibility floor:** focus `/blog/` first because it is the lowest tracked accessibility score at 83; target 95+.
4. **Move from branded discovery to non-brand discovery:** use GSC query rows to decide whether fractional CTO, CTO-as-a-service, AI MVP, technical-DD, or founder-guide pages are getting impressions before creating more URLs.
5. **Keep GEO source-building cadence:** publish source-backed, practitioner-specific posts and keep `llms.txt`, JSON-LD, internal links, and FAQ schema updated so AI engines have quotable facts.
6. **Defer thin location/vertical pages:** build a differentiated vertical/location page only when there is proof, local angle, and indexing momentum; avoid doorway-page risk.

## Blockers to report

- **Search Console / Bing manual verification and indexing remain the biggest blocker**, even though the automation can now read some GSC data. Current visibility is still tiny and mostly branded.
- **AI/GEO mentions and citations remain at 0%.** This likely will not move until source discovery and non-brand rankings improve.
- **Accessibility remains below target** on blog pages, especially `/blog/` at 83.
