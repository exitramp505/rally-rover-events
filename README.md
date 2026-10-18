# Rally Rover Events

Independent community-event guides and original merchandise. The site currently includes three December 5, 2026 parade guides: Georgetown TX, Flower Mound TX, and Richmond VA.

**Repository/source of truth:** https://github.com/exitramp505/rally-rover-events

**Hosting transition (2026-10-18):**
- Netlify project created: https://app.netlify.com/projects/rally-rover-events
- Reserved production hostname: https://rally-rover-events.netlify.app/ — **not live until the first deploy is confirmed**.
- Existing GitHub Pages site remains available during the transition: https://exitramp505.github.io/rally-rover-events/
- Keep using the GitHub repository. When connected to Netlify for continuous deployment, pushes to `main` will publish the static files.

## Scope

Grok Bot and supporting agents discover and verify public event information, write independent event-guide content, generate original merchandise/promotional art, manage site publishing and QC, and report operating results.

**Organizer relationships belong to the owner alone.** Do not assign organizer outreach, correspondence, follow-up, tracking, or reminders to AI agents. The site links to official event pages, and each site's email interest form is **not** an organizer registration or a ticket.

## Site structure

- `build.py` generates root-level HTML files from the edited copy in `docs/copy/*_FINAL.md` and design outputs.
- `img/` contains published image assets. Committed JPG files are retained when the original local design directory is absent.
- `docs/OPERATIONS.md`, `docs/DECISIONS.md`, `docs/STATUS.md` and `docs/QC_LOG.md` document active process and decisions.
- `docs/AGENT_COORDINATION.md` describes the **GitHub Issues handoff channel** for Grok Bot and ChatGPT.
- Links are relative, so the generated root works on GitHub Pages or a root-hosted site.

## Build and publish

The generated HTML/JPG files are already committed. For Netlify, use the GitHub repository `exitramp505/rally-rover-events`, production branch `main`, no build command, and publish directory `.` (repository root). This is also specified in `netlify.toml`.

When modifying event content:
```bash
pip install pillow
python3 build.py
git add -A
git commit -m "Update event content"
git push
```
If the original designer PNGs are not on the machine, the script keeps the existing committed JPGs. Review changes before pushing.

**Netlify setup remaining:** Connect this existing repo in https://app.netlify.com/projects/rally-rover-events to continuous deployment, select `main`, and verify the first deploy succeeds. After deployment, test every event page, store link, privacy page, and RSVP form. FormSubmit may require activation for the new origin; check `docs/STATUS.md`.

## Interest forms and privacy

FormSubmit sends consented interest-only submissions to the project inbox. The form stores the selected event, optional first name, email, and consent. These are not tickets, and are not registered with the event organizer. **Do not commit personal data, subscriber exports, or credentials.**

## Merchandise

Printful Quick Stores:
- Georgetown: https://rally-rover.printful.me
- Flower Mound: https://holidays-on-the-mound.printful.me
- Richmond: https://christmas-on-broad-street.printful.me

Approved prices: tees from $27, hoodies from $48, mugs $18, ornaments $16, totes $25, posters $26; $2 per size step from 2XL on tees and hoodies. Bundles have been discussed but are not yet active. Printful payout/tax setup remains owner-only.
