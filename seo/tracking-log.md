# SEO/GEO Tracking Log — souravchandra.com

Written by the Friday tracking automation. Read by the Monday publish automation
to inform keyword and topic selection. Newest entries at the top.

## How to add an entry (tracking automation must follow exactly)

For each tracked keyword, run web searches and record:
- SERP presence: does souravchandra.com appear in results for the keyword? Position if visible.
- Indexation: search `site:souravchandra.com` and note the number of indexed pages, and whether each blog URL appears.
- GEO/AI visibility: query the keyword phrased as a question and note whether souravchandra.com or "Sourav Chandra" is cited or mentioned in AI-generated answers or answer-engine style results.
- Competitors: note 2-3 domains that consistently outrank us per keyword.
- Actions for next publish run: 2-5 concrete recommendations (e.g., "target longer-tail variant X", "add FAQ schema to post Y", "post Z not indexed — check internal links").

## Tracked keywords

- fractional CTO Dubai
- fractional CTO UAE
- AI MVP development
- technical due diligence checklist
- how to hire a CTO (non-technical founder)
- CTO as a service Dubai
- (plus the primary keyword of every published post in blog/posts.json)

---

## 2026-07-06 — Week 0 tracking run (same-day as relaunch; treat as true baseline)

- Indexation: `site:souravchandra.com` returns 1 page (homepage only). Google's snapshot is STALE — it still shows the pre-relaunch "entrepreneur/rider, Bangalore, India" description, not the new fractional-CTO positioning. `/blog/` and `/blog/fractional-cto-dubai-uae-guide.html` are NOT indexed yet (expected: published today). sitemap.xml live and well-formed (3 URLs, application/xml); robots.txt live with AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.) allowed and sitemap declared.
- SERP presence: souravchandra.com absent from results for all 6 tracked keywords (fractional CTO Dubai, fractional CTO UAE, AI MVP development, technical due diligence checklist, how to hire a CTO, CTO as a service Dubai). Position: not visible anywhere. Expected at week 0.
- Competitors consistently ranking:
  - fractional CTO Dubai / UAE / CTO as a service Dubai: fractional-dubai.com, boardman.com, skynetcorp.ae, growthaccess.ae, kuchoriyatechsoft.com; a LinkedIn post ("Fractional CTO Dubai: Complete Cost & Benefits Guide") ranks for both head terms AND the cost question — individual content can rank here.
  - AI MVP development: appinventiv.com, upsilonit.com, tekrevol.com (agency listicles dominate; question-phrased long-tails like "build AI MVP in 30 days" surface smaller sites — rocketdevs.com, logiciel.io, catalect.io).
  - technical due diligence checklist: mev.com, mascience.com, circleci.com, akfpartners.com (high-authority; long-tail "checklist investors actually use" angle shows indie sites like kompella.io ranking).
  - how to hire a CTO (non-technical founder): karllhughes.com (personal site, #1 — proof a solo expert site can own this), trustshoring.com, startupgrind.com.
- GEO/AI visibility: 0/5. Neither souravchandra.com nor "Sourav Chandra" appears in answer-style results for: fractional CTO cost in Dubai, whether a UAE startup needs a fractional CTO, how to build an AI MVP fast, what a tech DD checklist includes, how a non-technical founder hires a CTO. Answer engines currently synthesize from fractional-dubai.com, solidmatics.com, karllhughes.com, kompella.io. Note: AED 15k–40k/month is the cost range engines repeat — our post should state a concrete range to be quotable.
- GSC: not connected — proxy signals only. Manual checklist in strategy.md still open (verify domain, submit sitemap). This is now the single highest-leverage unblock: without it we can't request indexing of the blog URLs or refresh the stale homepage snapshot.
- On-site audit: meta descriptions, canonicals, and Article/Person/Blog JSON-LD present on all 3 pages; internal links intact; no fixes needed this run.
- Comparison vs previous entry (baseline): no change expected same-day; homepage indexation confirmed but snapshot stale (new finding); blog URLs not yet crawled (new finding).
- Actions for next publish run (Monday):
  1. Proceed with queue item 2 (AI MVP development) but title/H1 it as the question long-tail "How to build an AI MVP in 30 days" — head term is agency-dominated, the 30-day angle is where small sites rank; include a concrete week-by-week scope and named stack (RAG, GPT-4/Claude API) so answer engines can quote it.
  2. Add FAQPage JSON-LD to the fractional-cto-dubai-uae-guide post covering "How much does a fractional CTO cost in Dubai?" with an explicit AED monthly range — that's the exact question engines answer today and none of the current sources are individuals with proof.
  3. In the new post, add 2-3 internal links to /blog/fractional-cto-dubai-uae-guide.html and to /#services (anchor text: "fractional CTO in Dubai") to accelerate crawl/indexation of the blog section.
  4. Homepage: Google's cached description is pre-relaunch. Once GSC is verified, request reindex of /, /blog/, and the post URL. (Flag for Sourav — cannot be automated until GSC is connected.)
  5. Theme rotation unchanged; note karllhughes.com as the model for the founder-guides theme (queue item 4) — personal-site E-E-A-T wins that SERP, so lean harder on first-person YC/Speechify proof there.

## 2026-07-06 — Baseline (setup day, no data yet)

- Site relaunched with blog at /blog/, sitemap.xml, robots.txt (AI crawlers allowed), JSON-LD (Person, ProfessionalService, Blog, Article).
- First post published: "Fractional CTO in Dubai & the UAE" (primary: fractional CTO Dubai).
- GSC not yet verified — proxy tracking only until Sourav completes the checklist in strategy.md.
- Actions for next publish run: proceed with queue item 2 (AI MVP development). No performance data to act on yet.
