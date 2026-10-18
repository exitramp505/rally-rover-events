# Operations

## Roles
- **Owner**: approves prices, money/tax/bank items, and new channels. Owns all contact and relationships with event organizers personally.
- **Coordinator bot (Grok Bot)**: researches and verifies public event information; maintains event records and briefs; manages QC, merchandise information, publishing, and operational reports. It does **not** contact organizers or manage organizer outreach.
- **Event Scriptwriter**: writes public event-guide and merchandise copy, captions, and short scripts from verified sources.
- **Event Designer**: creates original flyers, social graphics, merch art, and mockups.
- **Merch Ops**: manages Printful Quick Stores, prices, size adjustments, approved merchandise, and order-related operational checks. Owner handles sensitive payout/tax setup.
- **ChatGPT**: may review documentation, code, site behavior, and GitHub handoffs when invoked. No continuous monitoring is implied.

## Organizer relationships — expressly outside AI scope
The owner alone handles organizer contact and relationships. Do not initiate, draft, send, schedule, track, or remind anyone about organizer outreach, organizer replies, or organizer follow-ups. Do not create tasks, CRM records, or alerts for this purpose.

Bots may independently verify **public** event details, link to the event's official page, and correct inaccurate public guide information. Rally Rover's interest signup is not an official ticket or an organizer registration.

## Change-notice process
When a verified public event fact or merchandise price changes: update the event record, notify the Scriptwriter and Designer of the old and new public facts, replace affected published materials, log the correction, and report the change to the owner. Cancellations and postponements should be reflected promptly. No organizer contact or outreach tracking is part of this process.

## QC process
Use the checklist in `docs/DECISIONS.md` item 7. Log quality checks in `docs/QC_LOG.md`. Verify factual accuracy, prices, original licensed art, and the independent-guide disclosure. Never place attendee details, customer personal information, secrets, or API keys in GitHub.

## Site updates and hosting
GitHub is the source of truth. Generated HTML and images are committed in the repository root.
- Edit `docs/copy/` or `build.py`, run `python3 build.py` where Pillow is installed, inspect the generated files, and commit and push.
- The intended production host is **Netlify** with Netlify's `netlify.toml` build command that copies committed HTML and `img/` to a `dist/` publish directory (avoiding the publication of internal repository documents).
- Netlify automatic publishing begins only after the repository is connected to the Netlify site. See `docs/STATUS.md` for the current deployment state.
- Moving the public domain requires reactivating/testing the FormSubmit form on the new origin; verify with a test submission and do not assume it works.

## AI-to-AI coordination
See `docs/AGENT_COORDINATION.md`. Use GitHub Issues for work requests and responses, and repository documents for durable decisions. A GitHub issue is a shared mailbox, not a real-time connection: each agent must explicitly read/check the issue before it can respond.
