# Status (2026-10-18)

## Live
- Site on GitHub Pages: https://exitramp505.github.io/rally-rover-events/ (home, georgetown, flower-mound, richmond, privacy).
- Printful stores live with approved prices (see README).
- Eventbrite: account locked, listings unpublished. Do not retry.

## Open items (need Lysander)
- **Printful W-9 declined**: needs a hand-signed form or time-stamped e-signature. Only Lysander can do it (signature/tax details).
- **Payout bank account not set** in Printful; payout minimum $25/month via Stripe.
- Decide on Luma (suggested: one Georgetown test event, stop at first warning) and Facebook (needs his login; local groups require admin approval for selling). See `channels_research.md`.
- Bundles not available in Quick Stores; decide whether to drop or use another approach.
- Final decision on long-term hosting (Pages is fine for now).
- Eventbrite locked: no action unless he wants to appeal.

## RSVP form: how to view / export
- Signups arrive as emails (subject "Rally Rover RSVP signup") in `rallyrover@mail.grokbot.com`. A bot can search them (SearchEmailThreads) and compile a CSV of email, first_name, event, consent.
- Keep any exported list out of git.
- To delete a person: delete their email(s) from the inbox/export; they can also request deletion by emailing the inbox.
- To delete the test entry (email test-signup@example.com, event "TEST ENTRY"), delete that email from the inbox and ignore it in exports.
- Form is activated for origin `https://exitramp505.github.io/rally-rover-events/`. If the site moves to a new domain, submit once from the new site; FormSubmit emails an activation link to the inbox; click it. The alias in `build.py` (FORM_ID) may change.
- FormSubmit is not a mailing list tool: sending bulk email later needs an email platform (free tiers exist), and every message needs a working unsubscribe.
