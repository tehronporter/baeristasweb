from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import json
R=Path(__file__).resolve().parents[1];A=R/'assets';f=TTFont(str(A/'fonts/DisplayItalic.ttf'));gs=f.getGlyphSet();cm=f.getBestCmap()
pen=SVGPathPen(gs);x=0
for ch in 'Baeristas':
 gn=cm[ord(ch)];gs[gn].draw(TransformPen(pen,(1,0,0,1,x,0)));x+=f['hmtx'][gn][0]
path=pen.getCommands()
for name,col in [('pink','#C92E64'),('espresso','#34201F'),('cream','#FFF8F2')]:
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-50 -20 {x+100} 1100" role="img" aria-label="Baeristas"><path fill="{col}" transform="translate(0 850) scale(1 -1)" d="{path}"/></svg>'
 (A/f'wordmark-{name}.svg').write_text(svg)
heart='M50 90 C33 74 0 48 0 26 C0 0 33 -10 50 12 C67 -10 100 0 100 26 C100 48 67 74 50 90 Z'
for name,col in [('pink','#C92E64'),('espresso','#34201F'),('cream','#FFF8F2')]:
 for seam in [False,True]:
  line='<path d="M49 18 C73 40 27 47 50 72" fill="none" stroke="#FFF8F2" stroke-width="4"/>' if seam else ''
  (A/f'{"bean-heart" if seam else "heart"}-{name}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-5 -5 110 100" role="img" aria-label="Baeristas heart"><path fill="{col}" d="{heart}"/>{line}</svg>') if not (seam and name=='cream') else None
(A/'heart-pattern.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="600" height="600"><defs><pattern id="p" width="100" height="100" patternUnits="userSpaceOnUse"><path transform="translate(35 35) scale(.3)" d="{heart}" fill="#C92E64"/></pattern></defs><path fill="#F7DCE4" d="M0 0H600V600H0z"/><path fill="url(#p)" d="M0 0H600V600H0z"/></svg>')
tokens={'cream':'#FFF8F2','blush':'#F7DCE4','cherry-pink':'#C92E64','espresso':'#34201F','muted-berry':'#78535E','border':'#E7CDD2'}
(A/'brand-tokens.json').write_text(json.dumps({'colors':tokens,'fonts':{'display':'Cormorant Garamond','body':'DM Sans'}},indent=2))
(A/'brand-tokens.css').write_text(':root {\n'+''.join(f'  --brand-{k}: {v};\n' for k,v in tokens.items())+'  --font-display: "Cormorant Garamond", serif;\n  --font-body: "DM Sans", sans-serif;\n}\n')
print('Outlined wordmarks, symbols, pattern, and tokens exported.')
