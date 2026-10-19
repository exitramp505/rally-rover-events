# Fourthwall (merch provider)

**Decision:** Fourthwall replaces Printful. Confirmed by Lysander on 2026-10-18. Merch must be integrated into our own event pages, not sent to a separate store. One Fourthwall shop, "Rally Rover", with 3 collections (one per annual event). Tote price is $27.

**Environments:** GitHub Pages = preview (auto-deploys on push). Netlify = manual release only (commit message must carry `[publish-netlify]`; do NOT use that tag for normal commits).

**Secrets:** none in this repo. Never commit tokens or logins. `.gitignore` blocks `fourthwall_api.txt` and `fourthwall_login.txt`.

## Endpoints (non-secret)
- Shop admin: https://admin.fourthwall.com/store/rally-rover/
- Storefront (hosted checkout lives here): https://rally-rover-shop.fourthwall.com
- Storefront API base: https://storefront-api.fourthwall.com/v1/
  - Auth: `?storefront_token=<token>` (read-only catalog token). `GET /v1/collections` returned 200.
  - Products in a collection: `GET /v1/collections/{handle}/products?storefront_token=...`

## Collections
Intended handles: `georgetown`, `flower-mound`, `richmond`.
Verified via API on 2026-10-18 (9 PM ET): `/v1/collections` returns only **All Products** (`slug: all`). The three event handles return **404 Collection not found**, so they are not yet visible via the API (not created, hidden, or empty). `all` reports 4 items but lists 0, so nothing is live yet. Re-verify after products are uploaded and published; handles must match exactly.
Collection URLs on the storefront (once live): https://rally-rover-shop.fourthwall.com/collections/{handle}

## Planned design
- `build.py` fetches `/v1/collections/{handle}/products` at build time and emits static HTML product cards on each event page (that event's collection only).
- Buy button goes to the cart/checkout link; checkout is hosted by Fourthwall (can be styled, and put on our domain later).
- Build needs env var `FOURTHWALL_STOREFRONT_TOKEN`. If it is missing, build must skip the cards and keep the Printful links.
- Printful links stay until Fourthwall checkout is verified end to end.

## Token setup (Lysander does this)
1. GitHub: repo Settings > Secrets and variables > Actions > New repository secret. Name `FOURTHWALL_STOREFRONT_TOKEN`, value = the Storefront token.
2. Netlify: Site configuration > Environment variables > Add variable. Key `FOURTHWALL_STOREFRONT_TOKEN`, same value.
3. Token source: Fourthwall admin > Settings > For Developers > Headless (Storefront token, read-only).

## Prices (current)
| Item | Price |
|---|---|
| Tee | $27 (+$2 per size from 2XL) |
| Hoodie | $48 (+$2 per size from 2XL) |
| Tote | $27 |
| Poster | $26 |
| Mug | $18 |
| Ornament | $16 |

Merch shows the year only, no date. Customers pay shipping on top.

## Status
- Shop "Rally Rover" exists; collections and products are not yet published.
- Payouts (Stripe, tax, bank) pending, Lysander's to complete. Agents do not enter these.

## Merch integration (built 2026-10-18)
- `build.py` adds a **Merch** section (`#merch`) to each event page: cards with image, title, "From $X", size prices (tee/hoodie), and a Buy button linking to the Fourthwall product page (`https://rally-rover-shop.fourthwall.com/products/<slug>`). Each page shows only its own collection.
- Source order: (1) live Storefront API `/v1/collections/{handle}/products` using token from env `FOURTHWALL_STOREFRONT_TOKEN` (or local `/workspace/fourthwall_api.txt`, git-ignored); (2) **PREVIEW fallback** `data/merch_preview.json` when the API returns nothing (products are still hidden). Token is never written to output.
- Handles in `HANDLES` (build.py): `georgetown-christmas-stroll`, `flower-mound-christmas-parade`, `richmond-christmas-parade`. **Unverified**: all return 404 while collections are hidden/empty. Re-check `/v1/collections` after publishing and fix `HANDLES` if the slugs differ.
- Preview badge: set `MERCH_PREVIEW_BADGE=1` at build to show a small "Preview" badge on fallback cards. Off by default.
- Preview images are in `img/merch/` (mockups from design-trial where they exist; tote and poster use design preview PNGs, not real mockups). Replace with Fourthwall images automatically once the API returns products.
- Product slugs in the preview JSON are assumed (`georgetown-christmas-stroll-2026-<type>`, `holidays-on-the-mound-2026-<type>`, `christmas-on-broad-street-2026-<type>`); confirm against real Fourthwall slugs.
- Cart/checkout is via the product page for now. No GitHub Actions workflow added; Pages deploys from the branch. To build with live data in CI later, add repo secret `FOURTHWALL_STOREFRONT_TOKEN` (Lysander).
