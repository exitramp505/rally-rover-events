# Operations

## Roles
- **Lysander** (owner): approves prices, money/tax/bank items, new channels. Has said: fix wrong live info first and tell him after; cancellation/postponement takedowns also immediate.
- **Coordinator bot ("Grok Bot")**: owns event master record, briefs, QC checkpoint, QC_LOG, store prices, publishing, reports to Lysander. Each brief must include facts, current prices, vibe note and (if city-tied) city note, and is sent with priority true.
- **Event Scriptwriter**: promo post, short caption, 30-second script per event. Files in `docs/copy/*_FINAL.md`. Ends with the disclaimer.
- **Event Designer**: flyers, social graphics, merch art and mockups (outputs live in `/workspace/design-trial/` on the box; flyers have the disclaimer as last line).
- **Merch Ops**: Printful Quick Stores, prices, size upcharges, bundles, payouts (W-9 / bank blocked, see STATUS).

## Change-notice process
When any fact or price changes: update the master record, send a change notice (what changed, old and new values) to Scriptwriter and Designer, they re-issue corrected pieces immediately, coordinator replaces anything already published or sent, logs it, informs Lysander afterwards. Rebuild this site (`python3 build.py`) and push.

## QC process
Checklist is in `DECISIONS.md` item 7. Log each event: what was published, what failed review, what was fixed; flag repeated problems from one bot. Current log: `QC_LOG.md` (so far: Scriptwriter passed first try on all three; flyers failed once for missing disclaimer, passed round 2).

## Site updates
Edit copy in `docs/copy/`, run `python3 build.py`, commit, push. Pages redeploys in about a minute.
