# Status (updated 2026-10-18)

## Current site
- **Netlify production deploy READY (2026-10-18 7:41 PM ET)**: https://rally-rover-events.netlify.app/ (dashboard: https://app.netlify.com/projects/rally-rover-events). Netlify confirms deploy `6ad55915143f31df8690c44d`, GitHub branch `main`, commit `dae8ab000533d1895fdda080ae80dd34c668bdba`, no reported build errors, five HTML pages and fifteen assets published.
- GitHub Pages remains available as the previous host: https://exitramp505.github.io/rally-rover-events/ . Netlify is the production host; GitHub remains source of truth. **GitHub Pages is the designated development/demo site** (not the transaction platform). The repo's `netlify.toml` now requires a `[publish-netlify]` release marker for intentional Netlify production builds; gate verification is pending.
- **Still to test:** public homepage/event/privacy routes and images in a browser, official event links and Printful links, and interest form submission from the Netlify origin. The available HTTP checker could not retrieve the new host even though Netlify reports a ready published deploy. Reactivate FormSubmit if its new-origin verification requires it.
- Home has event cards only. Each event page has its own event-specific interest form and one footer disclaimer.
- **Fourthwall migration ordered**: Grok Bot has an account/store setup and product migration assignment in https://github.com/exitramp505/rally-rover-events/issues/3. Fourthwall account, catalog, integration and checkout are **not yet verified**. Printful stores still hold the currently published products and must remain usable through transition.
- Eventbrite account was locked; events were unpublished. Do not retry to circumvent the lock.

## Owner-only boundaries
- All organizer contact and relationships, replies, follow-ups and reminders are solely the owner's responsibility. AI must not manage these.
- Existing Printful W-9 was declined and the payout bank account was not configured. With a Fourthwall migration planned, owner should first decide how to handle any Printful sales/payouts and keep required records. Fourthwall account verification/tax/banking is owner-only.

## Other open operational items
- Decide whether to use Luma/Facebook distribution, subject to the respective terms and actual organizer status. No AI organizer outreach.
- Existing Printful Quick Stores cannot natively provide approved bundles. Evaluate Fourthwall's bundle capability, costs, and product coverage rather than making new Printful changes.
- Netlify Git connection and first deploy are complete. The new `[publish-netlify]` ignore rule for demo-only commits is committed but **its behavior has not yet been tested**. Public end-to-end tests and FormSubmit new-origin activation/testing remain pending.
- GitHub Issues handoff: https://github.com/exitramp505/rally-rover-events/issues/1. New decisions sent to Grok: GitHub Pages demo / Netlify production, Fourthwall account migration, and a request to configure an event-triggered GitHub issue-notification routine. **Grok previously acknowledged Issue #1** and said automatic issue-comment notification is unavailable in its then-current setup. Latest instructions (Fourthwall, GitHub Pages demo/Netlify controlled production) were posted afterward; Grok acknowledgement of those newer instructions and any working trigger remain pending.

## Interest form data
- Signups arrive as emails with a subject identifying the event at the Rally Rover project inbox. The signup means event/merch updates only, **not** official event registration.
- Do not commit exports or personal information to GitHub.
- The origin was activated for the GitHub Pages URL. Changing domains can require a fresh FormSubmit activation email to the inbox and a test submission.
- For suppression/deletion requests, remove the information from collected records. Bulk email, if used later, needs an unsubscribe process.

## Update 2026-10-18: hosting gate
- Lysander paused Netlify auto-publishing on 2026-10-18. GitHub Pages is the preview (updates on every push); Netlify is manual final publish only.
- Printful remains the merch provider. No Fourthwall decision has been made.
- Organizer outreach is owner-only (no AI drafting, sending, or tracking).
- Issue #1 acknowledged by the Grok Bot side. Grok Bot-side agents cannot be auto-notified of issue comments; the owner should tell it to check.

## Current migration priorities
1. Grok Bot: create or prepare owner-controlled Fourthwall account; pause for verification/tax/payouts; log non-sensitive setup status in issue #3.
2. Grok Bot: reconstruct event collections from print-ready design sources, compare margins/shipping, test store checkout; replace Printful links only when ready.
3. Grok Bot: test GitHub-to-Grok issue notification routine and Netlify release-marker gate. Do not run unnecessary production deploys.
4. Owner: personally retains organizer outreach; no AI reminders or communications in that category.

## Fourthwall status
Shop created, event collections not yet live via API, payouts pending (Lysander). Details: [FOURTHWALL.md](FOURTHWALL.md).
