---
name: Beyond Doubt
description: A monochrome jersey studio built from the supplied brand and garment imagery.
colors:
  ink: "#21221F"
  chalk: "#EDEDE8"
  muted: "#60615A"
  line: "#CDCEC6"
  dot: "#B8BAB1"
typography:
  title:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "calc(40 * var(--u))"
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.025em"
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "max(12px, calc(14 * var(--u)))"
    lineHeight: 1.6
  label:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "11px"
    fontWeight: 500
    lineHeight: 1.62
    letterSpacing: "0.12em"
  index:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: "max(30px, calc(50 * var(--n)))"
    fontWeight: 200
    lineHeight: 1
    letterSpacing: "-0.04em"
rounded:
  square: "0"
  circle: "50%"
spacing:
  tight: "8px"
  control-gap: "12px"
  control-inline: "18px"
  mobile-edge: "20px"
  drawer-mobile: "25px"
  drawer-edge: "44px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.chalk}"
    typography: "{typography.label}"
    rounded: "{rounded.square}"
    padding: "0 18px"
    height: "44px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.square}"
    padding: "0 18px"
    height: "44px"
  button-round:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.circle}"
    width: "44px"
    height: "44px"
  view-selector:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.label}"
    padding: "0 17px"
    height: "44px"
---

# Design System: Beyond Doubt

## Overview

**Creative North Star: "Monochrome jersey studio"**

This system supports the separate Beyond Doubt rebrand in `index-beyond-doubt.html`. The supplied italic wordmark and real garment photography carry the identity. A quiet neutral field, fine rules and compact controls keep attention on the printed artwork.

The original `index.html` is a separate reusable template. Its spacious composition and orbit interaction are retained for this rebrand, as requested by the user. Exact route composition belongs in the surface brief and design plan.

**Key Characteristics:**

- Actual wordmark and garment imagery.
- Chalk field with carbon ink and fine neutral rules.
- Spacious collection presentation with restrained controls.
- Continuous orbit, pointer parallax and front/back inspection.

## Colors

### Primary

Carbon ink is the foreground, active indicator, primary shop action and focus color. The clothing artwork supplies the expressive color.

### Neutral

Chalk is the page and drawer ground. Muted ink supports descriptions and secondary labels. The line color separates store rows and outlines secondary controls; the dot color marks inactive collection positions.

**The Artwork Color Rule.** Use the actual garment graphics as the principal color source in this storefront. Keep surrounding controls in the documented neutral palette.

## Typography

Inter is loaded from Google Fonts, with the declared system sans fallback. The brand display voice is the supplied wordmark image; do not recreate it as ordinary text.

Product titles use a stronger weight than descriptions. At the reference desktop size they render at 40px; portrait mobile uses 28px and short landscape uses 22px. Descriptions use a 30em maximum measure and reflow below the garment on portrait mobile. Drawer headings use 34px, store rows 18px, and address/body text 14px. Stock/profile notes use 12px.

The compact uppercase navigation is retained from the user-pinned template. Functional labels have an 11px floor; individual labels use tracking from 0.12em to 0.25em. The collection number is light and tabular because it identifies the current garment in sequence.

## Layout

The collection occupies one viewport. A centered stage scales from a 1440×900 reference using `--u`; chrome scales with viewport width using `--n`. The document does not scroll, while the business drawer and short landscape detail panel provide local scrolling.

Portrait layouts at widths up to 820px and heights from 521px use a 600×1100 stage reference. Product details stack below the garment, peripheral location labels recede, and collection controls remain at the bottom. Pause/play sits above previous/next; the exploration hint sits above both. Collection chrome is hidden during detail inspection to reserve room for product actions.

Short layouts up to 520px high retain a two-column detail arrangement with a bounded scrollable information panel. Wordmark size reduces again below 380px wide. The business drawer is full width on phones and capped at 530px on wider screens.

## Elevation & Depth

Garment alpha silhouettes carry a soft downward shadow. A subdued floor shadow anchors the orbit, and the drawer separates from the stage with a soft shadow and darkened backdrop. There is no card grid.

Product assets use the matching 2000px original photographs, with preview alpha guides refined against full-resolution contours. Each front/back PNG is 1000×1000 with the garment occupying 87.2% of the canvas, preserving the existing stage scale. Native garment detail spans approximately 770–815 pixels; mild output sharpening preserves the actual prints and fabric texture. Do not rebuild imagery from the 500px previews.

Orbit position determines scale, rotation and overlap depth. Pointer movement offsets the wordmark and garments at different rates. Entrance, side changes and detail transitions form one coordinated motion language. Pause stops automatic rotation; manual exploration remains available. Reduced-motion preference starts the collection paused and suppresses entrance, bounce and side/detail transitions.

## Shapes

Store actions and the mobile motion control have square corners. Previous/next and close controls are circles. Fine borders communicate control boundaries; active front/back selection uses a stronger underline. Garments retain silhouettes from the supplied transparent imagery.

## Components

### Shopping actions

The primary Shopee link uses filled ink with chalk text. Lazada uses a transparent secondary treatment. Both have a minimum 44px height, drawn outbound arrows, and a clear hover/focus response. They lead to the supplied brand shops, not fabricated product URLs.

### Collection controls

Previous/next buttons use consistent drawn line icons inside 44px circular targets. Pause/play has a text label and pressed state; on portrait phones it has its own visible outlined target. It remains keyboard accessible.

### Front/back selector

Two radio buttons select actual paired asset views. The selected view uses ink and a two-pixel underline; the other uses muted text and a fine rule. Arrow keys move between the views.

### Navigation and business drawer

The top-left wordmark returns home; About opens the native business dialog and Shop links to Shopee. Store rows in the drawer use typography and fine separators. Address, telephone and profile information follow. The dialog supports Escape, a close button and focus restoration to About.

### Product orbit

Five unique designs appear as interactive garment buttons. Drag, scroll and previous/next change the collection position; selecting a garment opens its front/back details. Product names describe the artwork without asserting official model names, prices or specifications.

## Do's and Don'ts

- **Do** use the supplied wordmark and real front/back product imagery.
- **Do** preserve the original template file when extending this rebrand.
- **Do** retain visible pause/play and usable shop controls at supported mobile sizes.
- **Do** use the neutral tokens for chrome and allow product artwork to carry color.
- **Don't** invent business founding dates, prices, sizes, availability or product specifications.
- **Don't** replace the user-pinned orbit with a conventional product grid without a new brief.
- **Don't** document dormant template colors or unused bag/swatch styles as Beyond Doubt primitives.
