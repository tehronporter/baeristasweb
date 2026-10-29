# Baeristas — proposed branding and website mockup

The work follows the requested order: research, a refreshed branding kit PDF, then a local responsive website mockup. This is a new proposed identity rather than an existing official brand manual.

## Review

1. `branding/Baeristas_Brand_Kit.pdf` — 16-page branding kit.
2. `branding/previews/contact-sheet.jpg` — overview of all brand pages.
3. `website-mockup/index.html` — local responsive website mockup. Open directly in a browser, or serve as below.
4. `website-mockup/previews/1440.png`, `768.png`, `390.png` — rendered desktop/tablet/mobile views.

## Run the mockup

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory website-mockup
```

Open http://127.0.0.1:4173 . No install/build step, API keys, or online font service required. The mockup intentionally uses simple HTML/CSS/JS rather than a production framework; the supplied document's Next.js instructions are background for a later implementation, not necessary for a visual mockup.

## Edit

- `website-mockup/index.html`: copy, locations, links and page structure.
- `website-mockup/style.css`: brand colors, type, responsive layout.
- `website-mockup/script.js`: mobile navigation and keyboard behavior.
- `branding/assets/`: reusable vector artwork, tokens and font files/licenses.
- `branding/source/build_brandkit.py`: editable PDF source. Requires Python `reportlab`.
- `branding/source/export_assets.py`: vector/font-outline asset generator. Requires Python `fonttools`.
- `website-mockup/assets/make_illustrations.py`: editable SVG illustration source.

## Scope and facts

The website includes drink categories, brand story, both reported stands and real Maps directions URLs. Menu products/prices, reviews, opening hours, ordering links, contact details and unresolved social links are not invented. NE details need owner confirmation. Illustrations are visibly conceptual and a short drinks note makes that explicit. Preview is excluded from search indexing. No production structured data or canonical domain is guessed.

See `RESEARCH.md`, `ASSETS.md`, `OWNER_CHECKLIST.md` and `VALIDATION.md`. No site was registered or deployed.
