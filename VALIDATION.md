# Validation — October 29, 2026

## Branding PDF

- Generated 16-page vector PDF using ReportLab with embedded fonts.
- Rendered every page and inspected a contact sheet.
- Checked text bounding boxes: no text outside page boundaries.
- Adjusted the creative-direction panel after visual inspection.
- Verified key small-text color pairs: espresso/cream, berry/cream, cream/cherry pink exceed 4.5:1.

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

No public deployment was performed.
