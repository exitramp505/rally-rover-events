# Status (2026-10-18)

## Current site
- **Netlify production deploy READY (2026-10-18 7:41 PM ET)**: https://rally-rover-events.netlify.app/ (dashboard: https://app.netlify.com/projects/rally-rover-events). Netlify confirms deploy `6ad55915143f31df8690c44d`, GitHub branch `main`, commit `dae8ab000533d1895fdda080ae80dd34c668bdba`, no reported build errors, five HTML pages and fifteen assets published.
- GitHub Pages remains available as the previous host: https://exitramp505.github.io/rally-rover-events/ . Netlify is the intended production host; GitHub remains source of truth.
- **Still to test:** public homepage/event/privacy routes and images in a browser, official event links and Printful links, and interest form submission from the Netlify origin. The available HTTP checker could not retrieve the new host even though Netlify reports a ready published deploy. Reactivate FormSubmit if its new-origin verification requires it.
- Home has event cards only. Each event page has its own event-specific interest form and one footer disclaimer.
- Printful stores are published at the prices in README.
- Eventbrite account was locked; events were unpublished. Do not retry to circumvent the lock.

## Owner-only boundaries
- All organizer contact and relationships, replies, follow-ups and reminders are solely the owner's responsibility. AI must not manage these.
- Printful W-9 was declined and needs the owner's hand-signed form or suitable time-stamped e-signature.
- Printful payout bank account not set; this requires owner involvement.

## Other open operational items
- Decide whether to use Luma/Facebook distribution, subject to the respective terms and actual organizer status. No AI organizer outreach.
- Printful Quick Stores cannot natively provide approved bundles; keep inactive unless a compliant alternative is selected.
- Netlify Git connection and first deploy are complete. Public end-to-end tests and FormSubmit new-origin activation/testing remain pending.
- GitHub Issues handoff created at https://github.com/exitramp505/rally-rover-events/issues/1 (see `docs/AGENT_COORDINATION.md`). Grok Bot has not yet acknowledged.

## Interest form data
- Signups arrive as emails with a subject identifying the event at the Rally Rover project inbox. The signup means event/merch updates only, **not** official event registration.
- Do not commit exports or personal information to GitHub.
- The origin was activated for the GitHub Pages URL. Changing domains can require a fresh FormSubmit activation email to the inbox and a test submission.
- For suppression/deletion requests, remove the information from collected records. Bulk email, if used later, needs an unsubscribe process.
