"""Baeristas / bubbly Y2K fashion identity / twelve-page editable brand guide."""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit,ImageReader
R=Path(__file__).resolve().parents[1]
for name,file in [('Body','Body.ttf'),('Bold','BodyBold.ttf'),('Black','BodyBlack.ttf'),('Script','LobsterTwo-BoldItalic.ttf')]:pdfmetrics.registerFont(TTFont(name,str(R/'assets/fonts'/file)))
C=json.loads((R/'palette.json').read_text())['colors'];W,H=1000,700
c=canvas.Canvas(str(R/'Baeristas_Brand_Kit.pdf'),pagesize=(W,H),pageCompression=1)
c.setTitle('Baeristas — Your daily little crush. | Y2K Brand Kit');c.setAuthor('Baeristas design proposal / prepared for Tehron Porter')
n=0

def rect(x,y,w,h,color='white',r=0,stroke=None,width=1):
 c.setFillColor(HexColor(C[color]));c.setStrokeColor(HexColor(C[stroke or color]));c.setLineWidth(width)
 if r:c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=bool(stroke))
 else:c.rect(x,H-y-h,w,h,fill=1,stroke=bool(stroke))
def txt(s,x,y,size=12,font='Body',col='blue',align='left'):
 c.setFillColor(HexColor(C[col]));c.setFont(font,size)
 getattr(c,{'left':'drawString','center':'drawCentredString','right':'drawRightString'}[align])(x,H-y-size*.82,s)
def para(s,x,y,w,size=14,col='blue',font='Body',leading=None):
 leading=leading or size*1.5
 for i,l in enumerate(simpleSplit(s,font,size,w)):txt(l,x,y+i*leading,size,font,col)
def line(x,y,x2,y2,col='blue',width=1):
 c.setStrokeColor(HexColor(C[col]));c.setLineWidth(width);c.line(x,H-y,x2,H-y2)
def label(s,x,y,col='blue'):txt(s.upper(),x,y,9,'Bold',col)
def heart(x,y,size,col='hot-pink',outline=None):
 c.saveState();c.translate(x,H-y);c.scale(size/100,size/100);p=c.beginPath();p.moveTo(50,-90);p.curveTo(33,-74,0,-48,0,-26);p.curveTo(0,0,33,10,50,-12);p.curveTo(67,10,100,0,100,-26);p.curveTo(100,-48,67,-74,50,-90);c.setFillColor(HexColor(C[col]));c.setStrokeColor(HexColor(C[outline or col]));c.setLineWidth(4);c.drawPath(p,fill=1,stroke=bool(outline));c.restoreState()
def star(x,y,size,col='white'):
 c.saveState();c.translate(x,H-y);c.scale(size/100,size/100);p=c.beginPath();p.moveTo(50,0);p.curveTo(54,-45,100,-50,100,-50);p.curveTo(54,-55,50,-100,50,-100);p.curveTo(46,-55,0,-50,0,-50);p.curveTo(46,-45,50,0,50,0);c.setFillColor(HexColor(C[col]));c.setStrokeColor(HexColor(C['blue']));c.setLineWidth(1.5);c.drawPath(p,fill=1,stroke=1);c.restoreState()
def script(s,x,y,size=80,col='hot-pink',sticker=False):
 if sticker:
  txt(s,x+3,y+5,size,'Script','blue')
  c.saveState();c.setStrokeColor(HexColor(C['white']));c.setFillColor(HexColor(C[col]));c.setLineWidth(size*.045);c.setLineJoin(1)
  t=c.beginText(x,H-y-size*.82);t.setFont('Script',size);t.setTextRenderMode(2);t.textOut(s);c.drawText(t);c.restoreState()
 else:txt(s,x,y,size,'Script',col)
def start(section,bg='white'):
 global n
 n+=1;rect(0,0,W,H,bg)
 label('BAERISTAS / Y2K DESIGN PROPOSAL',44,25,'white' if bg=='blue' else 'blue')
 txt(section.upper(),956,25,9,'Bold','white' if bg=='blue' else 'blue','right')
def end(bg='white'):
 col='white' if bg=='blue' else 'blue';line(44,652,956,652,col,.6);txt('THREE COLORS. ONE WHOLE MOOD. / OCTOBER 2026',44,670,8,'Bold',col);txt(f'{n:02}',956,669,9,'Bold',col,'right');c.showPage()
def title(labelText,heavy,scriptText=None):
 label(labelText,44,80);txt(heavy,44,108,43,'Black')
 if scriptText:script(scriptText,44,158,57)
def box(n,h,b,x,y,w=265):
 label(n,x,y);txt(h,x,y+26,26,'Black');para(b,x,y+69,w,13)
def image(path,x,y,w,h):c.drawImage(ImageReader(str(path)),x,H-y-h,width=w,height=h,preserveAspectRatio=True,anchor='c',mask='auto')
def cup(x,y,scale=1,sleeve='hot-pink'):
 c.saveState();c.translate(x,H-y);c.scale(scale,scale)
 p=c.beginPath();p.moveTo(-85,0);p.lineTo(85,0);p.lineTo(61,-239);p.curveTo(20,-256,-20,-256,-61,-239);p.close();c.setFillColor(HexColor(C['white']));c.setStrokeColor(HexColor(C['blue']));c.setLineWidth(1);c.drawPath(p,fill=1,stroke=1)
 p=c.beginPath();p.moveTo(-78,-70);p.lineTo(78,-70);p.lineTo(68,-166);p.curveTo(20,-181,-20,-181,-68,-166);p.close();c.setFillColor(HexColor(C[sleeve]));c.drawPath(p,fill=1,stroke=0)
 c.setFillColor(HexColor(C['blue']));c.roundRect(-95,0,190,18,7,fill=1,stroke=0);c.roundRect(-79,16,158,8,3,fill=1,stroke=0)
 c.setFillColor(HexColor(C['white']));c.setFont('Script',35);c.drawCentredString(0,-130,'Baeristas');c.restoreState()

start('01 / Your daily little crush.','baby-pink')
rect(31,65,938,562,'baby-pink',35,'blue',1.5)
label('FEMININE. BUBBLY. A LITTLE EXTRA.',72,99)
script('Baeristas',78,177,162,sticker=True)
star(795,130,95);heart(827,386,70,'hot-pink','white')
txt('YOUR DAILY',79,391,57,'Black');script('little crush.',76,447,91,'blue')
para('A pink-and-blue fashion crush for Portland’s personality-led coffee stop.',650,535,264,17)
end()
start('02 / Creative direction');title('THE NEW DIRECTION','BIG PERSONALITY.','Soft, bubbly energy.')
para('A Y2K women’s fashion mood: rounded script, bold italic type, sticker outlines, hearts, and a little star power. Keep the attitude playful and the palette disciplined.',45,245,880,20)
for a in [('01 / FEMININE','Plump & playful','Soft corners, buoyant script lettering, and a confidently pink point of view.',44),('02 / FASHION','A little extra','White outlines and blue offset shadows turn key words into sticker-like signatures.',358),('03 / COHESION','Less color. More identity.','Three colors repeat everywhere. Every graphic earns its place.',672)]:
 box(a[0],a[1],a[2],a[3],382,277)
para('Preview first: use original vector cups and graphics now. Approved company photography can replace illustrations in the real build.',44,607,904,12)
end()
start('03 / The palette');title('THREE BRAND COLORS + WHITE','KEEP THE COLOR STORY','sweet & simple.')
for i,(name,key,use) in enumerate([('Hot pink','hot-pink','Logo / large accents'),('Baby pink','baby-pink','Main soft surface'),('Blue','blue','All text / buttons'),('White','white','Space / outlines')]):
 x=44+i*231;rect(x,253,215,188,key,22,'blue');txt(name,x,462,24,'Black');txt(C[key],x,499,13,'Bold');para(use,x,531,212,12)
line(44,577,956,577)
para('Use blue for body text, navigation, and buttons. White on blue and blue on baby pink pass normal-text contrast. Hot pink is a graphic accent and logotype color; keep small text blue.',44,597,894,12)
end()
start('04 / Logo system','baby-pink');label('THE SIGNATURE',44,83);script('Baeristas',76,147,151,sticker=True)
label('PRIMARY / WHITE EDGE + BLUE OFFSET',82,338)
rect(44,397,440,182,'white',24,'blue');script('Baeristas',81,435,79);label('FLAT / HOT PINK ON WHITE',82,550)
rect(510,397,446,182,'blue',24);script('Baeristas',549,435,79,'white');label('REVERSE / WHITE ON BLUE',550,550,'white')
para('Proposed wordmark, based on Lobster Two Bold Italic. Clear space: one lowercase “a” height. Minimum width: 150 px / 38 mm. Keep the supplied proportions and outline-to-shadow relationship.',44,605,910,11)
end()
start('05 / Typography');title('TWO FAMILIES. DISTINCT ROLES.','CONFIDENT TYPE.','Bubbly curves.')
rect(44,253,440,307,'baby-pink',25,'blue');txt('DM SANS',72,284,43,'Black');txt('BLACK / 900',74,348,11,'Bold');para('Short, bold, tightly spaced headlines. Italic in the website for a sporty Y2K fashion feel.',74,391,362,17);txt('BODY / 400 + 600',74,500,11,'Bold')
rect(510,253,446,307,'white',25,'blue');script('Lobster Two',540,294,59,'blue');label('BOLD ITALIC / 700',543,383);para('The signature script. Use for the wordmark and one expressive phrase per section. Never for addresses, body copy, or small labels.',543,420,360,16)
para('Mobile scale: 47 px bold hero + 78 px script; 44 px section titles; 12–13 px body; 10–12 px actions. Adjust to fit the screen without squeezing words. Use generous line-height for practical copy.',44,594,904,12)
end()
start('06 / Graphic language');title('THE STICKER DRAWER','A LITTLE SPARKLE.','A lot of restraint.')
for x in [44,356,668]:rect(x,249,286,259,'baby-pink',24,'blue')
heart(139,300,94,'hot-pink','white');label('01 / HEART',66,475)
star(451,297,100);label('02 / FOUR-POINT SPARKLE',378,475)
rect(697,324,223,75,'blue',37);rect(692,318,223,75,'white',37,'blue',2);script('cute energy',710,334,39,'blue');label('03 / CAPSULE STICKER',689,475)
for x,b in [(44,'Use one heart or sparkle per composition. Avoid dense decorative scatter.'),(356,'Blue edges unify the system. White outlines keep graphics crisp.'),(668,'Round corners, thin blue rules, and a small blue offset make every piece feel related.')]:para(b,x,536,276,14)
end()
start('07 / Voice');title('THE WORDS MATCH THE LOOK','BUBBLY. CONFIDENT.','A little flirty.')
rect(44,251,558,266,'baby-pink',25,'blue');txt('YOUR DAILY',72,290,45,'Black');script('little crush.',70,349,87,sticker=True)
for y,h,b in [(256,'Too cute to skip.','Graphic statement'),(346,'Cute cup. Big energy.','Small sticker / social moment'),(436,'Find your stand.','Keep the useful action plain')]:script(h,640,y,35,'blue');para(b,642,y+49,280,12)
para('Use short, original lines with a wink. Keep directions, hours, ingredients, and location details straightforward. No invented testimonials, recipes, employee biographies, or operational claims.',44,575,900,15)
end()
start('08 / Mobile first');title('THE FIRST SCREEN IS THE CAMPAIGN','MADE FOR THE','phone crush.')
phone=R.parent/'website-mockup/previews/mobile-first-screen.png'
rect(643,70,279,562,'blue',35);rect(650,77,265,548,'white',29)
if phone.exists():image(phone,659,91,247,521)
for y,h,b in [(267,'01 / One complete opening','Brand, message, artwork, and visit action read together without a giant headline taking over.'),(379,'02 / Thumb-friendly actions','A clear visit button, readable labels, and an easy mobile menu. No permanent bar over the hero.'),(492,'03 / Shorter, richer scrolling','Compact drink cards, a strong graphic story moment, and immediately usable location cards.')]:
 label(h,44,y);para(b,44,y+29,500,16)
end()
start('09 / Desktop translation');label('SAME IDENTITY. MORE ROOM.',44,80);txt('ONE DESIGN LANGUAGE.',44,109,44,'Black')
desk=R.parent/'website-mockup/previews/desktop-first-screen.png'
rect(44,189,912,400,'baby-pink',24,'blue')
if desk.exists():image(desk,54,199,892,380)
para('Desktop expands the hero into a two-column campaign composition. The same colors, lettering, cup artwork, rounded controls, and sticker details remain intact.',44,612,904,12)
end()
start('10 / Cup concepts','baby-pink');label('A BRAND YOU CAN HOLD',44,84);txt('CUTE CUP.',44,119,58,'Black');script('Big energy.',44,179,84,'blue');star(813,100,87)
cup(290,339,1.05);cup(720,284,1.25,'blue');label('01 / PINK SLEEVE',73,600);label('02 / BLUE SLEEVE',642,600)
txt('Original concept illustrations. Production dimensions, inks, materials and dielines require supplier proofs.',44,627,9,'Body')
end()
start('11 / Social moments');title('THE SAME CRUSH, EVERYWHERE','BUILT FOR A','double take.')
for x,bg in [(44,'baby-pink'),(356,'white'),(668,'blue')]:rect(x,253,286,286,bg,25,'blue')
script('Baeristas',64,275,43,sticker=True);script('Too cute',67,367,51,'blue');script('to skip.',67,421,57,'blue');heart(257,466,35,'hot-pink','white')
label('THE DAILY CRUSH',380,279);cup(500,326,.63);script('Big energy.',380,483,43)
label('PORTLAND, OREGON',691,279,'white');script('See you,',689,350,55,'white');script('sweet thing.',688,413,49,'white');star(892,479,28,'baby-pink')
for x,b in [(44,'Short line. One outlined wordmark.'),(356,'Original cup artwork for the preview.'),(668,'Blue brings contrast, not another palette.')]:para(b,x,567,280,12)
end()
start('12 / Handoff');title('ONE COHESIVE SYSTEM','READY FOR THE','next little crush.')
rows=[('DELIVERED','12-page kit; script/sticker wordmarks; hearts and sparkles; three-color tokens; font files and licenses; responsive website preview; editable source.'),('PREVIEW SCOPE','Original drink illustrations remain intentional design assets. Real drink, staff and storefront photography can be commissioned for the production build.'),('OWNER CONFIRMATIONS','Preferred brand name, final logo treatment, approved business copy, both stands, current hours, menu/ingredients, social handle and photo permissions.'),('SOURCE & PROVENANCE','Palette follows the user-supplied current Instagram artwork, simplified at the user’s request. Typography and designs are proposed. Business research is documented in RESEARCH.md. Fonts: Lobster Two and DM Sans, SIL Open Font License.')]
for i,(h,b) in enumerate(rows):
 y=267+i*89;line(44,y-13,956,y-13);label(h,44,y);para(b,301,y,645,13)
end();c.save();print('12-page Y2K brand kit generated.')
