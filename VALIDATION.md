# Validation — October 29, 2026

## Branding PDF

- Generated 16-page vector PDF using ReportLab with embedded fonts.
- Rendered every page and inspected a contact sheet.
- Checked text bounding boxes: no text outside page boundaries.
- Updated all 16 pages to the current pink-and-blue colorway and inspected refreshed renders.
- Verified key small-text color pairs: navy/paper, muted/paper, paper/magenta exceed 4.5:1.

## Website mockup

Tested in headless installed Google Chrome using Playwright at 390×1000, 768×1000, and 1440×1000 viewport sizes.

- No horizontal page overflow at all three sizes.
- All local anchor targets exist.
- Both Maps URLs contain the expected encoded full destination addresses. Destination parameters verified; external Maps navigation not independently tested on a phone.
- No browser JavaScript errors or HTTP asset failures.
- Mobile disclosure menu opens and closes, Escape closes it and restores focus, and selecting a navigation link closes it.
- Rendered and visually inspected desktop, tablet and mobile layouts.
- Full-page screenshots explicitly load all lazy illustrations before capture.
- Fonts served locally; no third-party font request required.
- Reduced-motion CSS disables smooth scrolling and transitions.
- Website remains a review mockup. No production build pipeline or backend exists, so framework lint/type/build checks are not applicable. Current business facts, real photography and phone-based device behavior need owner review before public launch.

Initial mockup validation preceded deployment. GitHub Pages publication was subsequently requested by the user.

## Current colorway refresh

Repeated responsive browser and navigation checks after recoloring. Key normal-text pairs: navy/paper 11.38:1, muted/paper 10.50:1, muted/bubblegum 5.79:1, navy/sky-blue 4.76:1, paper/magenta 6.14:1. Category labels use navy so they also pass on the blue panel. Focus outlines use navy. Reference hot pink is reserved for artwork/accent use; it is not used as a small-text background. All PDF pages, full-page screenshots and downloadable packages were regenerated.
