from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import json
R=Path(__file__).resolve().parents[1];A=R/'assets'
colors=json.loads((R/'palette.json').read_text())['colors']
f=TTFont(A/'fonts/LobsterTwo-BoldItalic.ttf');gs=f.getGlyphSet();cm=f.getBestCmap();pen=SVGPathPen(gs);x=0
for ch in 'Baeristas':
 gn=cm[ord(ch)];gs[gn].draw(TransformPen(pen,(1,0,0,1,x,0)));x+=f['hmtx'][gn][0]
path=pen.getCommands()
for file in A.glob('*.svg'):file.unlink()
heart='M50 90 C33 74 0 48 0 26 C0 0 33 -10 50 12 C67 -10 100 0 100 26 C100 48 67 74 50 90 Z'
for name,key in [('pink','hot-pink'),('blue','blue'),('white','white')]:
 col=colors[key]
 (A/f'wordmark-{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-70 0 {x+140} 1000" role="img" aria-label="Baeristas"><path fill="{col}" transform="translate(0 750) scale(1 -1)" d="{path}"/></svg>')
 (A/f'heart-{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 -5 110 100"><path fill="{col}" d="{heart}"/></svg>')
(A/'wordmark-sticker.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-100 -30 {x+300} 1100" role="img" aria-label="Baeristas"><g transform="translate(0 750) scale(1 -1)"><path transform="translate(24 -32)" fill="{colors["blue"]}" stroke="{colors["blue"]}" stroke-width="70" stroke-linejoin="round" d="{path}"/><path fill="{colors["hot-pink"]}" stroke="white" stroke-width="55" stroke-linejoin="round" paint-order="stroke fill" d="{path}"/></g></svg>')
star='M50 0Q54 45 100 50Q54 55 50 100Q46 55 0 50Q46 45 50 0Z'
(A/'sparkle.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path fill="{colors["blue"]}" d="{star}"/></svg>')
(A/'heart-pattern.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600"><defs><pattern id="p" width="100" height="100" patternUnits="userSpaceOnUse"><path transform="translate(35 35) scale(.25)" d="{heart}" fill="{colors["hot-pink"]}"/></pattern></defs><path fill="{colors["baby-pink"]}" d="M0 0H600V600H0z"/><path fill="url(#p)" d="M0 0H600V600H0z"/></svg>')
(A/'brand-tokens.json').write_text(json.dumps({'colors':colors,'fonts':{'script':'Lobster Two Bold Italic','body':'DM Sans','headline':'DM Sans Black Italic'}},indent=2))
(A/'brand-tokens.css').write_text(':root {\n'+''.join(f'  --brand-{k}: {v};\n' for k,v in colors.items())+'  --font-script: "Lobster Two", cursive;\n  --font-body: "DM Sans", sans-serif;\n}\n')
print('Three-color Y2K brand assets exported.')
