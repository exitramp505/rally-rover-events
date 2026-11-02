# Analytics (GoatCounter)

Chosen 2026-11-02. Cookieless, privacy-friendly page-view counting on every page of the site.

## Why GoatCounter
- **Free, including small businesses.** GoatCounter.com terms: "currently offered for free for reasonable public usage. Running your personal website or small-to-medium business on it is fine" (only millions of pageviews/day are excluded). Merch sales are OK.
- **No cookies, no personal data stored** → no cookie banner needed.
- **Works on any static host** (GitHub Pages preview and Netlify production) with one script tag; no build plugin.
- **Read API** with scoped tokens, so the Grok Bot side can report visitors in the weekly report.
- Alternatives considered: Cloudflare Web Analytics (free, but needs a Cloudflare account + browser signup; API is GraphQL and less direct), Umami Cloud (free tier, but signup is browser-only), Plausible / Simple Analytics (paid).

## Setup (done)
- Account: `rallyrover` → dashboard https://rallyrover.goatcounter.com (owner email: the Rally Rover project inbox). Login and API token are kept privately on the Grok Bot box, never in this repo.
- API token `agent-read`: read statistics, export, read sites only (cannot change anything).
- Config: `data/analytics.json` (public values only: endpoint + script URL). Set `"enabled": false` to remove the tag.
- `build.py` adds `<script data-goatcounter="https://rallyrover.goatcounter.com/count" async src="https://gc.zgo.at/count.js">` to the `<head>` of all 5 pages (home, 3 events, privacy).

## What is tracked
- Page views, referrers (where visitors came from), browser/OS/screen size, country (from IP; IP is not stored).
- Click events:
  - `buy-<event>-<product>` on every merch **Buy** button.
  - `store-<event>` on the "More at our store" button.
  - `rsvp-submit-<event>` fired after a successful RSVP form submission (no email/name is sent).
- Both the GitHub Pages preview and Netlify production report into the same site; paths are the same (`/georgetown.html`, etc.). Our own test visits will count too. Adblockers hide some visitors.

## Reading the stats
- Dashboard: https://rallyrover.goatcounter.com (login required).
- API (Bearer token): `GET https://rallyrover.goatcounter.com/api/v0/stats/total?start=YYYY-MM-DD&end=YYYY-MM-DD`, `/api/v0/stats/hits` (per page), `/api/v0/stats/toprefs` (referrers). Docs: https://www.goatcounter.com/api
- For ChatGPT/GitHub Actions: create your own read-only token in the dashboard (User → API) and store it as a GitHub secret (e.g. `GOATCOUNTER_TOKEN`). Never commit it.

## Privacy
`privacy.html` states: anonymous page visits counted with GoatCounter, no cookies, no personal data stored.
