# Visibility Growth Reports — souravchandra.com

This directory tracks whether souravchandra.com is becoming more discoverable for fractional CTO, AI MVP, technical due diligence, and founder-guide queries.

## Files

- `search-visibility-daily.md` — Google Search Console metrics when the property is accessible; blockers are recorded explicitly.
- `pagespeed-weekly.md` — PageSpeed/Lighthouse mobile performance snapshots for homepage and strategic blog URLs.
- `expected-outcomes.md` — staged 30/60/90-day targets.
- `benchmark-scorecard.md` — current metrics compared against targets: current → target → status → action.
- `recurring-actions.md` — metric/research triggers mapped to follow-up actions.
- `raw/visibility-metrics.jsonl` — machine-readable records for trend analysis.

## Operating loop

1. Daily metrics collector records Search Console, PageSpeed, route/indexability health, and raw JSONL.
2. Daily benchmark scorer compares the latest metrics to expected outcomes.
3. Weekday AI/GEO and competitor/trend research should append evidence and open safe PRs for source-backed content, internal links, FAQ/schema, and title/meta improvements.

## Current caveats

- Search Console access is verified through `sc-domain:souravchandra.com`; daily automation prefers service account `sourav-gsc-visibility@pyza-website.iam.gserviceaccount.com` with user ADC only as fallback.
- PageSpeed requires the local `PAGESPEED_API_KEY` environment variable loaded by Hermes cron.
- Do not invent claims, client logos, testimonials, search-volume numbers, or credentials.
