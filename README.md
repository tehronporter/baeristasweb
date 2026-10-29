# Baeristas — bubbly Y2K preview

A feminine Y2K fashion direction with plump script, bold italic headlines, outlined stickers, and a tightly controlled palette: hot pink, baby pink, blue, and white. This is a design preview; original vector cups intentionally stand in for company photography until the real build.

Live review: https://tehronporter.github.io/baeristasweb/

## Review files

- `branding/Baeristas_Brand_Kit.pdf`: revised 12-page brand kit, including mobile/desktop applications.
- `branding/previews/contact-sheet.jpg`: all 12 pages at a glance.
- `website-mockup/index.html`: responsive website source.
- `website-mockup/previews/mobile-first-screen.png`: mobile opening at 390×844.
- `website-mockup/previews/{390,768,1440}.png`: full-page device previews.
- `branding/assets/`: proposed script/sticker wordmarks, hearts, sparkle, pattern, tokens, fonts and licenses.
- `branding/palette.json`: three brand colors and white.

## Run locally

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory website-mockup
```

Open http://127.0.0.1:4173 . No build, package installation, external font service or API key is needed.

## Edit and publish

- `website-mockup/index.html`: copy and layout structure.
- `website-mockup/style.css`: palette, typography and mobile-first composition.
- `website-mockup/script.js`: mobile menu and contextual visit bar.
- `website-mockup/assets/make_illustrations.py`: vector cup artwork source.
- `branding/source/build_brandkit.py`: editable PDF source (ReportLab).
- `branding/source/export_assets.py`: outlined logo assets and tokens (fontTools).
- `branding/source/package_review.py`: PDF page previews and downloadable ZIPs (Pillow, PyMuPDF).

GitHub Pages serves `main:/docs`. After website changes run `python3 scripts/prepare_pages.py`, commit the refreshed source and `docs/`, then push `main`. Brand-guide source and internal research are kept outside the Pages document root. The page remains excluded from search indexing while business details await confirmation.

## Preview behavior

The visit bar is hidden over the hero and while location cards are visible. It appears between those sections on phones, with consistent blue-and-white styling. Drink cards use compact horizontal layouts on phones. All normal text uses blue on white/baby pink, or white on blue. Pink lettering is reserved for large graphic statements and proposed wordmarks.

No fictional prices, reviews, employees, schedules, recipes, order endpoints or contact details are added. The two directions links use researched addresses; operating details still require owner confirmation. See `RESEARCH.md`, `ASSETS.md`, `OWNER_CHECKLIST.md`, and `VALIDATION.md`.
