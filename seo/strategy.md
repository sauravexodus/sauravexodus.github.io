# SEO/GEO Content Strategy — souravchandra.com

This file is the single source of truth for the automated weekly blog pipeline.
The Monday publish automation reads this file and `seo/tracking-log.md` before
writing anything. It updates the queue below after each publish.

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

## Content queue (publish automation: take the top unpublished item, then rotate themes)

| # | Status | Theme | Working title | Primary keyword |
|---|--------|-------|---------------|-----------------|
| 1 | PUBLISHED 2026-07-06 | fractional-cto-uae | Fractional CTO in Dubai & the UAE: costs, models, and when you actually need one | fractional CTO Dubai |
| 2 | QUEUED | ai-mvp | How to scope an AI MVP that ships in 30 days (and survives month two) | AI MVP development |
| 3 | QUEUED | tech-dd | The technical due diligence checklist investors actually use | technical due diligence checklist |
| 4 | QUEUED | founder-guides | Non-technical founder? How to keep a dev agency honest | non-technical founder building an app |
| 5 | QUEUED | trending-ai | (auto-discover: pick the week's most relevant AI development and give the CTO take) | (derive from topic) |
| 6 | QUEUED | fractional-cto-uae | Fractional CTO vs dev agency vs full-time hire: the real math for UAE startups | CTO as a service Dubai |

After item 6, continue rotating themes 1→5. Generate new working titles informed
by `seo/tracking-log.md` performance data: double down on themes/keywords that
are gaining impressions or AI-engine citations, deprioritize ones that are not.

## Publishing rules (automation must follow exactly)

1. One post per run. 1,200–1,800 words. Written in Sourav's voice (see homepage FAQ answers for tone reference).
2. Create `blog/<slug>.html` by copying the structure of an existing post (nav, blog.css, Article JSON-LD, meta/OG tags, canonical URL, CTA box). Slug: kebab-case from primary keyword.
3. Add a post card to `blog/index.html` immediately after the `<!-- POSTS:START` marker (newest first).
4. Append the post to `blog/posts.json` (top of the posts array).
5. Add a `<url>` entry to `sitemap.xml` and bump `<lastmod>` on `/` and `/blog/`.
6. Update the queue table above (mark PUBLISHED with date, ensure at least 3 QUEUED items remain — generate more if needed).
7. Commit with message `Publish: <title>` and push to origin master. Git must be run ON THE MAC (not the sandbox) so SSH keys are available.
8. GEO requirements per post: direct answer to the primary question within the first two paragraphs, descriptive H2/H3 headings phrased as questions where natural, concrete numbers and named entities, Article JSON-LD.

## Google Search Console (one-time manual step for Sourav)

- [ ] Go to https://search.google.com/search-console, add property `souravchandra.com` (Domain property, verify via DNS TXT record at your domain registrar).
- [ ] Submit sitemap: `https://souravchandra.com/sitemap.xml`.
- [ ] Optional: connect the GSC connector in Claude so the Friday tracking automation can pull real impressions/clicks instead of proxy checks.

Until GSC is verified, the tracking automation uses proxy signals (see tracking-log.md).
