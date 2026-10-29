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

## Mobile readability and sharing fixes

The supplied mobile screenshot exposed overly small practical text, a narrow card-copy column, a late primary action, decorative hearts that suggested inactive favorite controls, and a visit bar that could cover the closing/footer. The correction moves the full-width primary action above the illustration; uses 14–16 px copy, 14–15 px action labels, 16 px addresses and 12 px supporting notes; gives category copy 65% of the card; removes false controls, a crowded hero sticker and repeated story copy; and hides the floating bar whenever the hero, locations, closing or footer is visible. The mobile breakpoint now covers widths through 700 px.

Verified the revised opening in Chrome and WebKit at 390×844, with touch/mobile emulation: no overflow, and the primary visit action ends at approximately 432 px within the 844 px viewport. The ten-width layout checks, Escape/focus behavior, menu selection behavior, and contextual bar tests pass. Updated full-page captures use reduced-motion mode to prevent transient scrolling/opacity effects from appearing in the screenshots.

Sharing assets now include a 1200×630 branded PNG card, explicit Open Graph and Twitter large-image metadata with absolute HTTPS asset URLs, an SVG B monogram favicon, 32 px PNG fallback, and 180 px Apple touch icon. Image dimensions and referenced files are checked locally and after deployment. External apps may cache older link previews; no claim of forcing third-party caches to refresh is made.
