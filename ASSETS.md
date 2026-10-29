# Asset provenance — Y2K direction

The user requested a bubbly, feminine Y2K women’s fashion look and a smaller palette, using the supplied Instagram artwork as a color reference. The current system uses three brand colors: hot pink `#F72796`, baby pink `#F7BEDD`, and blue `#07569B`. White `#FFFFFF` is the sole neutral. Baby pink is a lightened companion to the reference, supporting readable blue text. No additional magenta, navy, berry, cream or sky-blue UI colors remain in the active system. Screen colors are approximations; physical production needs supplier proofs.

## Original design assets

- `branding/assets/wordmark-sticker.svg`: proposed outlined script wordmark, white edge and blue offset.
- `branding/assets/wordmark-{pink,blue,white}.svg`: flat outlined wordmarks, no installed font needed.
- `branding/assets/heart-*.svg`, `sparkle.svg`, `heart-pattern.svg`: matching vector graphic system. The previous coffee-bean seam motif is retired.
- `branding/assets/brand-tokens.{css,json}` and `branding/palette.json`: current color/type definitions.
- `website-mockup/assets/hero-cup.svg`: newly drawn paired-cup composition, orbit, heart, sparkle and capsule sticker.
- `website-mockup/assets/{espresso,smoothies,spritzers}.svg`: original vector category concepts. They do not represent approved menu recipes, cup production specifications or ingredient claims.
- Brand guide packaging/social compositions: original vector mockups, not print dielines.

No company photography, staff portraits, storefront photos, magazine photos or stock media are republished. No staff or storefront images are fabricated. The supplied screenshot is a reference only; its phone UI and business artwork are not republished.

## Fonts and licensing

- **Lobster Two Bold Italic**, 700: proposed wordmark and script accent. Source: https://github.com/google/fonts/tree/main/ofl/lobstertwo .
- **DM Sans**, 400 / 600 / 900: body, labels, and bold headings. Black is visually italicized in CSS for headline styling. Source: https://github.com/google/fonts/tree/main/ofl/dmsans .
- Both use the SIL Open Font License. Original font copyrights and license text are included with brand files and the standalone website assets.

All public website fonts are local. The SVG wordmarks and cup graphics contain outlined lettering. Source font files are included for editable design work. Typography and logo treatments remain proposals, with no formal trademark clearance claimed.

## Social sharing and app icon

`website-mockup/assets/social-share.png` is an original 1200×630 branded social card. `social-share.svg` is the editable, font-independent outlined source. `favicon.svg` uses a Baeristas script B monogram; `favicon-32.png` and `apple-touch-icon.png` are browser-rendered 32×32 and 180×180 variants. All use the same three-color system and white. Generate vector sources with `branding/source/build_social_assets.py`; raster exports are rendered from those SVGs in a browser. Open Graph/Twitter metadata reference the PNG by its actual GitHub Pages URL. No external social account or handle is invented.
