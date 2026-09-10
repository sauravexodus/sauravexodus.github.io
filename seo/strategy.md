# SEO/GEO Content Strategy — souravchandra.com

This file is the single source of truth for the evidence-backed editorial
pipeline. The weekday automation reads this file and `seo/tracking-log.md`
before drafting anything. It may prepare a complete draft pull request, but it
must not publish substantive editorial copy without Sourav's explicit approval.

Queue states are:

- `QUEUED` — eligible for the next editorial drafting slot.
- `DRAFT PR #N` — one integrated preview candidate exists; do not create a duplicate.
- `DEFERRED YYYY-MM-DD: reason` — a specific quality/evidence gate failed; advance to the next item rather than rediscovering it every week.
- `PUBLISHED YYYY-MM-DD` — merged and verified on the canonical site.

## Positioning (do not drift from this)

Sourav Chandra, fractional CTO for AI and early-stage startups. 2× YC founding
engineer, ex-Speechify lead engineer. Shipped to 1M+ users and $1M+/month.
Based in Sharjah/Dubai, UAE (GMT+4), working globally. Offers: Fractional CTO
Retainer, AI MVP Sprint, Technical Due Diligence. Audience: non-technical
founders, AI startup founders, investors. Voice: direct, experienced,
opinionated, "proof not promises," no fluff. Every post ends with the standard
CTA box linking to the free 30-min call.

## Keyword themes (approved 2026-07-06)

1. fractional-cto-uae — "fractional CTO Dubai", "fractional CTO UAE", "part-time CTO for startups", "CTO as a service Dubai", "startup CTO cost UAE"
2. ai-mvp — "AI MVP development", "how to build an AI product fast", "LLM app architecture", "AI product engineering", "RAG vs fine-tuning for startups"
3. tech-dd — "technical due diligence checklist", "startup tech DD for investors", "how VCs evaluate a codebase", "red flags in technical due diligence"
4. founder-guides — "how to hire a CTO", "non-technical founder building an app", "dev agency vs in-house team", "how to evaluate a dev shop quote"
5. trending-ai — auto-discovered each week via web search: current AI industry news, model releases, and debates where a fractional-CTO perspective adds value. Must still tie back to the audience above.

## Content queue (draft automation: take the top eligible item, then rotate themes)

| # | Status | Theme | Working title | Primary keyword |
|---|--------|-------|---------------|-----------------|
| 1 | PUBLISHED 2026-07-06 | fractional-cto-uae | Fractional CTO in Dubai & the UAE: costs, models, and when you actually need one | fractional CTO Dubai |
| 2 | PUBLISHED 2026-07-06 | ai-mvp | How to scope an AI MVP that ships in 30 days (and survives month two) | AI MVP development |
| 3 | PUBLISHED 2026-07-06 | tech-dd | The technical due diligence checklist investors actually use | technical due diligence checklist |
| 4 | PUBLISHED 2026-07-13 | founder-guides | Non-technical founder building an app? How to keep a dev agency honest | non-technical founder building an app |
| 5 | QUEUED | trending-ai | (auto-discover: pick the week's most relevant AI development and give the CTO take) | (derive from topic) |
| 6 | PUBLISHED 2026-07-21 | fractional-cto-uae | CTO as a service in Dubai: engagement models, an explicit AED pricing table, and how to choose (published ahead of item 5 per 2026-07-19 tracking action 1) | CTO as a service Dubai |
| 7 | QUEUED | ai-mvp | RAG vs fine-tuning: what your startup actually needs (and what each costs) | RAG vs fine-tuning for startups |
| 8 | QUEUED | tech-dd | How VCs evaluate a codebase (and what they never look at) | how VCs evaluate a codebase |
| 9 | QUEUED | founder-guides | How to evaluate a dev shop quote (the AED 300k question): line items that should be there, padding that should not, and the questions that shrink the number | how to evaluate a dev shop quote |

After item 6, continue rotating themes 1→5. Generate new working titles informed
by `seo/tracking-log.md` performance data, direct source research, and distinct
buyer questions. Absence of topical Search Console queries is a measurement
signal, not a permanent veto on drafting an already approved strategic topic.

## Drafting and publishing rules (automation must follow exactly)

1. Keep at most one open editorial candidate. Before drafting, inspect open PRs for `editorial/*` or a title prefixed `Editorial review:`. Update that candidate when required; never create a duplicate.
2. On an editorial slot, take the highest eligible queued item and prepare one complete 1,200–1,800-word post in Sourav's voice (see homepage FAQ answers for tone reference).
3. A draft must add a distinct buyer decision, operating model, or useful artifact beyond existing canonical pages. Repeated definitions, country-name swaps, annual-title churn, and unsupported market numbers fail the gate.
4. Use current direct sources and map claims to inline links. Never invent clients, testimonials, credentials, addresses, search volume, prices, outcomes, legal/compliance claims, or universal thresholds.
5. Create `blog/<slug>.html` using the established article structure: nav, blog.css, Article/FAQ JSON-LD where truthful, meta/OG tags, canonical URL, internal links, and CTA box. Slugs are kebab-case.
6. Integrate the candidate on the same branch: add the newest card to `blog/index.html`, prepend the record in `blog/posts.json`, add the sitemap URL, and update the queue state to `DRAFT PR #N` once the PR number exists.
7. Use branch `editorial/<slug>` and open a **draft pull request** titled `Editorial review: <title>`. Verify JSON-LD, JSON, XML, local route mappings, duplicate registry entries, links, tests/scripts, `git diff --check`, and added-line secret/unsafe-markup scans.
8. Automation must stop at `REVIEW REQUIRED`. It must not infer approval from CI, CodeRabbit, elapsed time, or silence, and it must not merge substantive public copy. Only an interactive session acting on Sourav's explicit approval may mark the PR ready, merge it, wait for GitHub Pages, and verify the canonical URL.
9. Report-only changes and narrowly mechanical technical fixes may follow the established low-risk auto-merge policy. New articles, material article sections, service/price/credential claims, and source interpretation may not.
10. If a queue item fails, record `DEFERRED YYYY-MM-DD: <exact reason>` and advance next cycle. Do not repeat `NO_PUBLISH` for the same frozen proposal without a changed evidence condition.
11. After an approved article is live, mark it `PUBLISHED YYYY-MM-DD`, keep at least three eligible queued items, and generate evidence-backed replacements when needed.
12. GEO requirements per post: answer the primary question within the first two paragraphs, use descriptive question-led H2/H3 headings where natural, include concrete decision criteria and named sources, and emit truthful Article structured data.

## Google Search Console (one-time manual step for Sourav)

- [x] Domain property `sc-domain:souravchandra.com` is verified and accessible to the visibility collector's service account (confirmed 2026-07-30; still returning authenticated data on 2026-09-01).
- [ ] Submit sitemap: `https://souravchandra.com/sitemap.xml`.
- [x] The daily visibility collector pulls authenticated impressions/clicks through the dedicated service account; no interactive GSC connector is required for cron.

Authenticated GSC collection is working. Sitemap submission/request-indexing completion is not recorded, so keep that separate from property access and continue using bounded proxy surfaces only for external SERP/AI visibility checks (see tracking-log.md).
