# QC log per event
## Georgetown / Flower Mound / Richmond
- 2026-10-18: Initial pages published by Event Merch Ops before QC checkpoint existed. No Scriptwriter/Designer pieces yet.
- 2026-10-18 Georgetown FINAL (scriptwriter): PASS. Facts match record (Sat Dec 5 2026, 10:00 AM, Historic Downtown, 45th, 75,000+), prices match live, disclaimer last line, buy link present. Not yet swapped onto Eventbrite page (awaiting Flower Mound/Richmond finals + designer visuals).
- 2026-10-18 Flower Mound/Richmond FINAL: files missing (only v1/v2 present); requested.

## 2026-10-18 – Georgetown Christmas Stroll Parade
- Price update applied: tote $25, poster $26, size upcharges +$2 from 2XL; approved by Lysander 2026-10-18 in chat; bundles not live. Eventbrite page now lists tee "from $27", hoodie "from $48", tote $25, poster $26.

## 2026-10-18 – Flower Mound Christmas Parade & Tree Lighting
- Price update applied: tote $25, poster $26, size upcharges +$2 from 2XL; approved by Lysander 2026-10-18 in chat; bundles not live. Eventbrite page now lists tee "from $27", hoodie "from $48", tote $25, poster $26.

## 2026-10-18 – Richmond Christmas Parade
- Price update applied: tote $25, poster $26, size upcharges +$2 from 2XL; approved by Lysander 2026-10-18 in chat; bundles not live. Eventbrite page now lists tee "from $27", hoodie "from $48", tote $25, poster $26.
- 2026-10-18 Flower Mound FINAL: PASS (facts match record: Sat Dec 5, festivities 5:30, parade 6:00, Gerault Park; prices live; disclaimer last line). Richmond FINAL: PASS (Sat Dec 5, 10:15 AM, 10th & Marshall, Broad St, 43rd; no sponsor names; prices live; disclaimer last). No review failures from Scriptwriter so far.
- 2026-10-18 Flyers (designer) round 1: FAIL on all 3 (missing disclaimer as last line); facts/prices/art pass. Sent back.
- 2026-10-18 Flyers round 2: PASS (disclaimer added; Georgetown viewed; others same fix). Flyers are drafts for Lysander, not yet posted anywhere.

## 2026-10-18 – Copy swap (Scriptwriter FINAL promo posts) – Georgetown / Flower Mound / Richmond
- Saved new description (structured content: Georgetown v10, Flower Mound v6, Richmond v6) via events/swap_copy.py: FINAL promo text, existing merch collage after intro, HTML price list, store link, official link, end-time-placeholder note, disclaimer as last plain line; removed IMPORTANT/unofficial/old promoter-disclosure blocks. Verified via API read-back that the new text is stored.
- NOT VERIFIED PUBLIC: public event pages still served the old text (checked repeatedly over ~3 min), and then the Eventbrite API token began returning 401 INVALID_AUTH, so republish/verify could not be completed. Follow-up needed: new token, then re-check public pages.

## 2026-10-18 – Eventbrite lock
- Eventbrite locked the account for Spam Policy violations and unpublished all three listings; the copy swap above never went public. Replaced by this static site (see DECISIONS.md).
