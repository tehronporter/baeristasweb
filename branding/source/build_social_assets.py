"""Create outlined, font-independent social card and app-icon SVGs."""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import json
R=Path(__file__).resolve().parents[2];A=R/'website-mockup/assets';C=json.loads((R/'branding/palette.json').read_text())['colors']
def letters(text,font):
 f=TTFont(R/'branding/assets/fonts'/font);gs=f.getGlyphSet();cm=f.getBestCmap();pen=SVGPathPen(gs);advance=0
 for ch in text:
  g=cm[ord(ch)];gs[g].draw(TransformPen(pen,(1,0,0,1,advance,0)));advance+=f['hmtx'][g][0]
 return pen.getCommands(),advance
def lettering(text,font,x,y,width,color,sticker=False):
 d,advance=letters(text,font);scale=width/advance
 if sticker:
  return f'<g transform="translate({x} {y}) scale({scale} {-scale})"><path d="{d}" transform="translate(25 -35)" fill="{C["blue"]}" stroke="{C["blue"]}" stroke-width="65" stroke-linejoin="round"/><path d="{d}" fill="{color}" stroke="white" stroke-width="44" stroke-linejoin="round" paint-order="stroke fill"/></g>'
 return f'<path d="{d}" transform="translate({x} {y}) scale({scale} {-scale})" fill="{color}"/>'
word=(A/'wordmark-sticker.svg').read_text().replace('<svg xmlns=', '<svg x="48" y="30" width="320" height="100" xmlns=',1)
cups=(A/'hero-cup.svg').read_text().replace('<svg xmlns=', '<svg x="675" y="108" width="485" height="453" xmlns=',1)
card=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630"><title>Baeristas — Your daily little crush.</title><rect width="1200" height="630" fill="{C['baby-pink']}"/><rect x="24" y="24" width="1152" height="582" rx="34" fill="none" stroke="{C['blue']}" stroke-width="2"/>{word}{lettering('YOUR DAILY','BodyBlack.ttf',60,250,500,C['blue'])}{lettering('little crush.','LobsterTwo-BoldItalic.ttf',57,373,572,C['hot-pink'],True)}{lettering('Portland’s bikini coffee stop.','BodyBold.ttf',61,474,458,C['blue'])}{lettering('Espresso. Smoothies. Energy spritzers.','Body.ttf',61,521,509,C['blue'])}{cups}</svg>'''
(A/'social-share.svg').write_text(card)
d,w=letters('B','LobsterTwo-BoldItalic.ttf');s=70/w
favicon=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><title>Baeristas</title><rect x="2" y="2" width="96" height="96" rx="24" fill="{C["baby-pink"]}" stroke="{C["blue"]}" stroke-width="3"/>{lettering("B","LobsterTwo-BoldItalic.ttf",15,80,65,C["hot-pink"],True)}</svg>'
(A/'favicon.svg').write_text(favicon)
print('Outlined social sharing image and favicon created.')
