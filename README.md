# Rally Rover Events

Independent community-event guides and original merchandise. The site currently includes three December 5, 2026 parade guides: Georgetown TX, Flower Mound TX, and Richmond VA.

**Repository/source of truth:** https://github.com/exitramp505/rally-rover-events

**Demo and production hosting (2026-10-18):**
- **Netlify published successfully:** https://rally-rover-events.netlify.app/ (dashboard: https://app.netlify.com/projects/rally-rover-events). Netlify reports production deploy `6ad55915143f31df8690c44d` in `ready` state, branch `main`, commit `dae8ab000533d1895fdda080ae80dd34c668bdba`.
- **GitHub Pages is the development/demo site**: https://exitramp505.github.io/rally-rover-events/ (not a commercial transaction endpoint).
- **Netlify is production.** To save Netlify deployment credits, the `netlify.toml` ignore command skips ordinary commits and allows intentional releases only when the latest commit message contains `[publish-netlify]`. This new gate still needs a verified skip/release test. GitHub remains source of truth; browser and FormSubmit tests remain open.

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

The generated HTML/JPG files are already committed. For Netlify, use the GitHub repository `exitramp505/rally-rover-events`, production branch `main`, the committed static files copied into a `dist` folder by the build command specified in `netlify.toml`. The publish directory is `dist`; do not configure a Python build.

When modifying event content:
```bash
pip install pillow
python3 build.py
git add -A
git commit -m "Update event content"
git push
```
If the original designer PNGs are not on the machine, the script keeps the existing committed JPGs. Review changes before pushing.

**Netlify status:** Connected to the GitHub repo; first production deploy successfully published on 2026-10-18. **Demo commits must not carry `[publish-netlify]`**, while an owner-approved release commit must carry it. The Netlify build copies committed HTML files and `img/` assets to `dist/` without rebuilding images. **Still verify** every public event page, store link, privacy page, and RSVP form in a browser. FormSubmit may require activation for the new origin; check `docs/STATUS.md`.

## Interest forms and privacy

FormSubmit sends consented interest-only submissions to the project inbox. The form stores the selected event, optional first name, email, and consent. These are not tickets, and are not registered with the event organizer. **Do not commit personal data, subscriber exports, or credentials.**

## Merchandise

**Migration decision:** The owner selected **Fourthwall** for all event merchandise. Grok Bot is assigned the owner-controlled Fourthwall account setup and migration in [Issue #3](https://github.com/exitramp505/rally-rover-events/issues/3). Do not assume the account, catalog, or website integration is already live. The current Printful Quick Stores remain operational until all equivalent Fourthwall links and checkout are verified.

Current transitional Printful Quick Stores:
- Georgetown: https://rally-rover.printful.me
- Flower Mound: https://holidays-on-the-mound.printful.me
- Richmond: https://christmas-on-broad-street.printful.me

Approved prices: tees from $27, hoodies from $48, mugs $18, ornaments $16, totes $25, posters $26; $2 per size step from 2XL on tees and hoodies. Bundles have been discussed but are not yet active. Fourthwall account verification, credentials, tax, identity and payout steps remain owner-only. Existing Printful financial obligations and historical orders must be preserved.

- **Merch provider:** see [docs/FOURTHWALL.md](docs/FOURTHWALL.md) (Fourthwall replaces Printful; Printful links remain until Fourthwall checkout is verified).
