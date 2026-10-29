# Y2K preview validation — October 29, 2026

## Mobile and responsive layout

Tested the redesigned website in installed Google Chrome with Playwright at 320, 360, 375, 390, 430, 600, 601, 768, 1024 and 1440 px widths (844 px viewport height).

- No horizontal document overflow at any tested width.
- No browser JavaScript errors or failed HTTP assets.
- Menu opens; Escape closes and restores toggle focus; selecting a navigation link closes the menu.
- Contextual mobile visit bar stays hidden over the hero, appears after the hero and hides while location cards are visible. Hidden state is also removed from the tab order and accessibility tree.
- Mobile opening reviewed at 390×844; full mobile/tablet/desktop pages rendered for visual review.
- All illustration images explicitly loaded before full-page capture.
- Normal text uses blue/white (7.46:1) or blue/baby pink (4.75:1). Blue buttons use white labels. Hot pink is for decorative marks and large lettering; no white small-text buttons on pink.
- Reduced-motion mode disables smooth scrolling and transitions. No continuous animation.
- Two Maps directions retain the original researched destinations; external routing behavior is not claimed to be phone-tested.

## Brand kit

Rebuilt as a new 12-page guide using Lobster Two Bold Italic and DM Sans, the three-color palette and white. Includes actual responsive preview compositions, logo/sticker treatments, graphic rules, voice, packaging and social examples. Rendered for inspection; fonts embedded. Text bounds checked against page edges.

## Scope

This is an intentionally illustrative preview. Actual company photography and final operational details can be supplied during the production build. No checkout, forms, fabricated menu prices, staff biographies, reviews or open-now status are introduced. Static HTML/CSS/JS requires no framework typecheck or production build.

GitHub Pages serves the public review from `main:/docs`. Deployment is verified after publication.
