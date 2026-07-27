# Recurring Growth Actions

| Date UTC | Trigger | Evidence | Action Taken | PR | Status | Follow-up Date |
|---|---|---|---|---|---|---|
| 2026-07-27 | GEO foundation gap | Local static check found `llms.txt` missing; robots.txt explicitly allowed GPTBot/OAI/ChatGPT/Claude/PerplexityBot/Google-Extended but not Perplexity-User, Applebot-Extended, or Bingbot. | Added root `llms.txt` with Sourav's services, proof, important URLs, and AI citation guidance; expanded robots.txt explicit AI/search crawler allowlist. | #2 | Merged and live verified | 2026-07-28 |
| 2026-07-27 | Discovery still blocked | Metrics collector returned GSC `BLOCKED_SITE_ACCESS`; sitemap and metadata are healthy but proxy SERP/GEO visibility remains absent. | Re-recorded blocker in reports; do not request OAuth because site access/verification, not token scope, is the blocker. | n/a | Needs Sourav GSC/Bing action | 2026-07-28 |
