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

## 2026-07-10 — Week 1 tracking run

- Indexation: `site:souravchandra.com` still returns 1 page (homepage only), and Google's snapshot is STILL the stale pre-relaunch "entrepreneur/rider, Bangalore, India" description. None of the 3 blog URLs from posts.json are indexed (`site:souravchandra.com/blog` returns zero pages from our domain) — 4 days after publish, Google has not crawled the blog section. sitemap.xml live and well-formed (application/xml, 5 URLs: /, /blog/, all 3 posts — matches posts.json). robots.txt live, AI crawlers (GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended) allowed, sitemap declared.
- SERP presence: souravchandra.com absent from results for all 6 tracked keywords (fractional CTO Dubai, fractional CTO UAE, AI MVP development, technical due diligence checklist, how to hire a CTO, CTO as a service Dubai). Unchanged from baseline; expected while unindexed.
- Competitors consistently ranking:
  - fractional CTO Dubai / UAE / CTO as a service Dubai: fractional-dubai.com (multiple URLs incl. its own articles), boardman.com/dubai, growthaccess.ae, kuchoriyatechsoft.com, skynetcorp.ae, ignyte.ae. NEW this week: golosnichenko.com — an individual practitioner's personal site with a dedicated /locations/fractional-cto-dubai page ranking top-5 for both head terms AND the cost question (second proof after karllhughes.com that a solo expert site can win these SERPs); digitalreference.co listicle "Best Fractional CTO & Outsourced CTO Services in the UAE" ranks for both head terms (outreach target: get listed); the LinkedIn cost post still ranks.
  - AI MVP development: tekrevol.com, appinventiv.com, cmarix.com, pixelplex.io (agency pages own the head term). The 30-day question long-tail is led by rocketdevs.com (#1), productschool.com, datafortune.com, iviewlabs.com — question-framed posts, exactly the format of our post, which just isn't indexed yet.
  - technical due diligence checklist: mev.com, mascience.com, circleci.com, akfpartners.com stable; techcxo.com, madewithlove.com, ringstonetech.com also visible. Investor-phrased variant surfaces sphereinc.com, dealroom.net, YC's Series A diligence checklist.
  - how to hire a CTO (non-technical founder): karllhughes.com still #1; trustshoring.com, startupgrind.com, startwisehires.com; kompella.io still visible for the founder+CTO working-relationship angle.
- GEO/AI visibility: 0/5 again. Neither souravchandra.com nor "Sourav Chandra" appears in answer-style results for: fractional CTO cost in Dubai (engines quote AED 15k–40k/mo, narrower 15k–25k band, sourced from fractional-dubai.com, kuchoriyatechsoft.com, now golosnichenko.com); whether a UAE startup needs a fractional CTO (boardman, smartdev, fractional-dubai; engines now also cite UAE-specific compliance angles — PDPL, UAE PASS); how to build an AI MVP in 30 days (rocketdevs, productschool, datafortune); tech DD checklist for investors (sphereinc, dealroom, YC library); how a non-technical founder hires a CTO (karllhughes, trustshoring, quicklyhire, kompella.io).
- GSC: not connected — proxy signals only. Manual checklist in strategy.md still open. Now the critical path: blog uncrawled after 4 days and the homepage snapshot is still pre-relaunch; only GSC verification lets us submit the sitemap and request (re)indexing.
- On-site audit + fixes applied this run: meta descriptions, canonicals, Article JSON-LD present on all pages; FAQPage JSON-LD confirmed live on the fractional-CTO guide (covers the Dubai cost question — last week's action 2 already shipped). Gap found: no cross-post body links from the AI MVP post or the fractional guide (only the tech-dd post had one). FIXED now: added "Related" contextual links so all 3 posts interlink (full crawl mesh, descriptive anchors), bumped their sitemap `<lastmod>` to 2026-07-10.
- Comparison vs previous entry: no movement on indexation, SERP, or GEO (expected at day 4 with the blog uncrawled). New competitor intel: golosnichenko.com proves the individual-site + location-page pattern works for our head terms; digitalreference.co listicle is a placement opportunity. Cost range engines quote (AED 15k–40k) unchanged — our guide states a concrete range and now needs indexing to compete for the citation.
- Actions for next publish run (Monday 2026-07-13):
  1. Publish queue item 4 (founder-guides, "non-technical founder building an app") as planned — karllhughes.com (#1) and kompella.io prove personal-site E-E-A-T wins this SERP. H1 phrased as a question, heavy first-person YC/Speechify proof, and FAQPage JSON-LD covering "How does a non-technical founder hire a CTO?" and "dev agency vs in-house team?".
  2. Add FAQPage JSON-LD to ai-mvp-development.html and technical-due-diligence-checklist.html, mirroring their existing question-phrased H2s (both SERPs are question-dominated; the fractional guide already has it).
  3. The new post must body-link all 3 existing posts + /#services with descriptive anchors ("fractional CTO in Dubai", "technical due diligence checklist", "AI MVP that ships in 30 days") to extend the crawl mesh from day one.
  4. Re-title/frame queue item 6 (CTO as a service Dubai) as a dedicated location/service hybrid page modeled on golosnichenko.com's /locations pattern, with an explicit AED pricing table (AED 15k–40k is the quotable range engines repeat) so it can compete for the cost citation.
  5. Flag for Sourav (cannot be automated): complete GSC verification + submit sitemap + request indexing of /, /blog/, and all 3 post URLs; also add the site to Bing Webmaster Tools (Perplexity/ChatGPT lean on Bing's index) and consider pitching digitalreference.co's UAE fractional-CTO listicle for inclusion.

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
