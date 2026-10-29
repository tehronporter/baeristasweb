"""Original vector product/sticker concepts using the three brand colors + white."""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import json
A=Path(__file__).parent
P=json.loads((A.parents[1]/'branding/palette.json').read_text())['colors']
F=TTFont(A/'LobsterTwo-BoldItalic.ttf');gs=F.getGlyphSet();cm=F.getBestCmap();pen=SVGPathPen(gs);advance=0
for ch in 'Baeristas':
 gn=cm[ord(ch)];gs[gn].draw(TransformPen(pen,(1,0,0,1,advance,0)));advance+=F['hmtx'][gn][0]
logo=pen.getCommands()
blue=P['blue'];pink=P['hot-pink'];baby=P['baby-pink']
def word(y,col):return f'<g transform="translate(-86 {y}) scale({172/advance} {-172/advance})"><path d="{logo}" fill="{col}"/></g>'
def cup(body,sleeve,logoColor,tilt,x,y,scale=1):
 return f'''<g transform="translate({x} {y}) rotate({tilt}) scale({scale})"><path d="M-106-139H106L77 171Q0 193-77 171Z" fill="{body}" stroke="{blue}" stroke-width="2"/><path d="M-99-64H99L87 69Q0 85-87 69Z" fill="{sleeve}"/>{word(21,logoColor)}<path d="M-104-149L-93-163H93L104-149Z" fill="{blue}"/><rect x="-117" y="-149" width="234" height="23" rx="8" fill="{blue}"/><path d="M-100-140H100" stroke="white" opacity=".45"/><path d="M-79 98L-73 153" stroke="white" stroke-width="4" opacity=".6"/></g>'''
def star(x,y,size,col='white'):
 return f'<path transform="translate({x} {y}) scale({size/100})" d="M50 0Q54 45 100 50Q54 55 50 100Q46 55 0 50Q46 45 50 0Z" fill="{col}" stroke="{blue}" stroke-width="2"/>'
hero=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 560"><defs><radialGradient id="glow"><stop stop-color="white" stop-opacity=".85"/><stop offset="1" stop-color="white" stop-opacity="0"/></radialGradient></defs><ellipse cx="302" cy="287" rx="260" ry="238" fill="url(#glow)"/><ellipse cx="300" cy="305" rx="274" ry="92" fill="none" stroke="{blue}" stroke-width="1.5" transform="rotate(-25 300 305)"/>{star(44,94,62)}{star(483,365,64)}{star(438,35,38,pink)}<ellipse cx="300" cy="486" rx="178" ry="14" fill="{blue}" opacity=".12"/>{cup('white',pink,'white',-14,211,292,.94)}{cup(baby,'white',blue,14,397,279,1.04)}<path d="M120 430C104 417 79 401 79 383C79 362 105 355 120 372C135 355 161 362 161 383C161 401 136 417 120 430Z" fill="{pink}" stroke="white" stroke-width="5"/><g transform="translate(376 447) rotate(-9)"><rect x="-96" y="-27" width="192" height="54" rx="27" fill="white" stroke="{blue}" stroke-width="2"/><text text-anchor="middle" y="5" font-family="Arial,sans-serif" font-size="13" font-weight="bold" letter-spacing="1" fill="{blue}">COFFEE + CHEMISTRY</text></g></svg>'''
(A/'hero-cup.svg').write_text(hero)
for name,tilt in [('espresso',-12),('smoothies',10),('spritzers',-8)]:
 body='white' if name!='smoothies' else baby;sleeve=pink if name!='spritzers' else blue
 graphic=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 360">{star(255,32,44)}{star(34,239,27,pink)}{cup(body,sleeve,"white",tilt,177,178,.79)}</svg>'
 (A/f'{name}.svg').write_text(graphic)
print('Y2K drink illustrations refreshed.')
