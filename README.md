# Rally Rover Events (static site)

Independent fan guides + merch for three community holiday parades on **Saturday, Dec 5, 2026**:
Georgetown TX, Flower Mound TX, Richmond VA. Each page has event info, a link to the official event page,
merch from a Printful Quick Store, and an interest-only RSVP form (email list for event/merch updates).
We are **not affiliated with or endorsed by the organizers**; every page ends with that disclaimer.

Live site: https://exitramp505.github.io/rally-rover-events/  
Repo: https://github.com/exitramp505/rally-rover-events

## Structure
- `build.py` generates every `*.html` file (home, 3 event pages, `privacy.html`) from copy in `docs/copy/*_FINAL.md` and flyer/mockup images. Edit `build.py` or the copy, run `python3 build.py`, commit the output.
- `img/` flyers and merch mockups actually used (JPG, resized by build.py from the designer's PNGs, which are not in the repo; the build skips image regeneration if the source folder is missing).
- `docs/` notes for humans and future AIs: `DECISIONS.md`, `OPERATIONS.md`, `STATUS.md`, `QC_LOG.md`, `channels_research.md`, `vibe_city_notes.md`, `copy/` (QC-passed Scriptwriter copy).
- All links are relative, so the folder can be hosted anywhere static (GitHub Pages now; Cloudflare Pages / Netlify / any host later).

## Build / deploy
```
pip install pillow      # only needed if regenerating images
python3 build.py        # env: FORM_ID (FormSubmit alias), DESIGN_DIR (source PNGs)
git add -A && git commit -m "..." && git push   # Pages serves branch main, root
```
GitHub Pages: Settings > Pages > Deploy from branch `main` `/ (root)`. Nothing else is host-specific.
To move hosts: publish the repo root on the new host, then re-activate the RSVP form (see `docs/STATUS.md`).

## RSVP form
Service: **FormSubmit** (formsubmit.co), free, no account. Each signup is emailed to the project inbox
`rallyrover@mail.grokbot.com`. Hidden honeypot `_honey`, required consent checkbox, thank-you state shown in-page.
The endpoint uses a random alias (in `build.py`), not the raw email. **Never commit collected emails** (`.gitignore` blocks csv/signups).

## Stores and prices (Printful Quick Stores)
| Event | Store |
|---|---|
| Georgetown | https://rally-rover.printful.me |
| Flower Mound | https://holidays-on-the-mound.printful.me |
| Richmond | https://christmas-on-broad-street.printful.me |

Tee from $27, Hoodie from $48, Mug $18, Ornament $16, Tote $25, Poster $26. Tees and hoodies +$2 per size step from 2XL
(Georgetown store tops out at 3XL). Bundles (tee+mug $42, ornament+mug $30) approved but NOT set up (Quick Stores lack native bundles).
Lead with hoodies and mugs in copy.

## Official event pages
Georgetown https://dgagtx.org/Parade · Flower Mound https://www.flowermound.gov/parade · Richmond https://www.richmondparade.org/
