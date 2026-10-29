from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import simpleSplit
import math,json
ROOT=Path(__file__).resolve().parents[1]
for n,f in [('Display','Display.ttf'),('Italic','DisplayItalic.ttf'),('Body','Body.ttf'),('Bold','BodyBold.ttf')]:pdfmetrics.registerFont(TTFont(n,str(ROOT/'assets/fonts'/f)))
W,H=1000,700
PALETTE=json.loads((ROOT/'palette.json').read_text())['colors']
C={**PALETTE, 'cream':PALETTE['paper'],'blush':PALETTE['bubblegum'],'pink':PALETTE['magenta'],'ink':PALETTE['navy'],'berry':PALETTE['muted'],'line':PALETTE['border']}
c=canvas.Canvas(str(ROOT/'Baeristas_Brand_Kit.pdf'),pagesize=(W,H),pageCompression=1)
c.setTitle('Baeristas | A little morning mischief | Proposed Brand Kit')
c.setAuthor('Baeristas branding concept / prepared for Tehron Porter')
page=0

def rect(x,y,w,h,col,r=0):
 c.setFillColor(HexColor(C.get(col,col)));c.setStrokeColor(HexColor(C.get(col,col)))
 if r:c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=0)
 else:c.rect(x,H-y-h,w,h,fill=1,stroke=0)
def text(s,x,y,size=12,font='Body',col='ink',align='left'):
 c.setFillColor(HexColor(C.get(col,col)));c.setFont(font,size)
 getattr(c,{'left':'drawString','right':'drawRightString','center':'drawCentredString'}[align])(x,H-y-size*.78,s)
def para(s,x,y,w,size=14,col='ink',font='Body',leading=None):
 leading=leading or size*1.5
 lines=simpleSplit(s,font,size,w)
 for i,l in enumerate(lines):text(l,x,y+i*leading,size,font,col)
 return y+len(lines)*leading

def line(x,y,x2,y2,col='line',width=1):
 c.setStrokeColor(HexColor(C.get(col,col)));c.setLineWidth(width);c.line(x,H-y,x2,H-y2)
def label(s,x,y,col='berry'):text(s.upper(),x,y,10,'Bold',col)
def heart(x,y,s,col='pink',seam=False):
 c.saveState();c.translate(x,H-y);c.scale(s/100,s/100)
 p=c.beginPath();p.moveTo(50,-90);p.curveTo(33,-74,0,-48,0,-26);p.curveTo(0,0,33,10,50,-12);p.curveTo(67,10,100,0,100,-26);p.curveTo(100,-48,67,-74,50,-90)
 c.setFillColor(HexColor(C.get(col,col)));c.drawPath(p,stroke=0,fill=1)
 if seam:
  p=c.beginPath();p.moveTo(49,-18);p.curveTo(73,-40,27,-47,50,-72);c.setStrokeColor(HexColor(C['cream']));c.setLineWidth(4);c.drawPath(p)
 c.restoreState()
def word(x,y,size=100,col='ink'):text('Baeristas',x,y,size,'Italic',col)
def start(section,bg='cream'):
 global page
 page+=1;rect(0,0,W,H,bg)
 label('BAERISTAS / BRAND CONCEPT',48,25,'cream' if bg=='ink' else 'berry')
 label(section,952,25,'cream' if bg=='ink' else 'berry') if False else text(section.upper(),952,25,10,'Bold','cream' if bg=='ink' else 'berry','right')
def end(bg='cream'):
 col='blush' if bg=='ink' else 'berry'
 line(48,652,952,652,'berry' if bg=='ink' else 'line',.6)
 text('PROPOSED IDENTITY • OCTOBER 2026',48,669,9,'Body',col)
 text(f'{page:02d}',952,669,10,'Bold',col,'right');c.showPage()
def title(k,h,sub=None):
 label(k,48,81);text(h,48,110,47,'Display')
 if sub:para(sub,50,174,850,14,'berry')
def bullet(n,h,b,x,y,w=260):
 text(n,x,y,11,'Bold','pink');text(h,x,y+27,25,'Display');para(b,x,y+68,w,13,'berry')
def cup(x,y,scale=1,body='cream',sleeve='pink'):
 c.saveState();c.translate(x,H-y);c.scale(scale,scale)
 c.setFillColor(HexColor('#B98FC3'));c.ellipse(-90,-262,90,-237,fill=1,stroke=0)
 p=c.beginPath();p.moveTo(-95,-15);p.lineTo(95,-15);p.lineTo(68,-242);p.curveTo(26,-258,-26,-258,-68,-242);p.close()
 c.setFillColor(HexColor(C[body]));c.drawPath(p,fill=1,stroke=0)
 p=c.beginPath();p.moveTo(-86,-83);p.lineTo(86,-83);p.lineTo(76,-180);p.curveTo(25,-192,-25,-192,-76,-180);p.close()
 c.setFillColor(HexColor(C[sleeve]));c.drawPath(p,fill=1,stroke=0)
 c.setFillColor(HexColor(C['ink']));c.roundRect(-107,-16,214,21,8,fill=1,stroke=0);c.roundRect(-91,2,182,10,4,fill=1,stroke=0)
 c.setFillColor(HexColor(C['cream']));c.setFont('Italic',36);c.drawCentredString(0,-139,'Baeristas')
 c.setFont('Bold',7);c.drawCentredString(0,-159,'A LITTLE MORNING MISCHIEF.')
 c.restoreState()

# 01
start('01 / Current colorway refresh','blush')
heart(811,116,90,'deep-blue',True)
label('PORTLAND, OREGON',52,129)
word(42,209,176,'pink')
text('A little morning',52,406,58,'Display');text('mischief.',52,467,64,'Italic','pink')
para('A feminine, flirtatious identity for a coffee stop with personality.',620,463,310,17)
text('BRAND STRATEGY / VISUAL IDENTITY / APPLICATIONS',52,602,10,'Bold')
end()
# 02
start('02 / Brand foundation');title('THE IDEA','Make the everyday irresistible.','A warm, expressive identity that turns a quick coffee run into a moment worth anticipating.')
rect(48,236,904,150,'ink',16)
para('For Portland coffee drinkers drawn to a playful experience, Baeristas is a woman-owned bikini coffee stop pairing drive-through convenience with a confident personality.',78,266,840,24,'cream','Display',33)
for a in [('01','Feminine','Bubblegum pink, sculptural lettering, and a vivid blue counterpoint.',48),('02','Self-assured','A confident invitation. The people behind the counter have agency.',360),('03','Easy to visit','The same care goes into legible menus, addresses, and directions.',672)]:bullet(a[0],a[1],a[2],a[3],433)
end()
# 03
start('03 / Research');title('EVIDENCE BEFORE AESTHETICS','A real identity. A new expression.')
rows=[('Woman-owned + bikini coffee','Published business advertising supports both attributes.','S1, S2, S3'),('Pink + playful personality','An indexed social bio describes a pink coffee house; the voice is cheeky.','S4'),('Vegan + drive-through positioning','Supported in ads. Current ingredients and menu still need confirmation.','S1, S2, S3'),('Current color reference','User-supplied current artwork pairs hot pink, bubblegum and blue. The older green ad is historical.','REF')]
y=220
for h,b,s in rows:
 line(48,y-13,952,y-13);text(h,48,y,22,'Display');para(b,390,y,455,12,'berry');text(s,950,y,10,'Bold','pink','right');y+=87
para('REF: The user supplied current pink-and-blue artwork on October 29, 2026. No public brand manual was located in this search. That does not establish that one never existed. Direct social access was limited; indexed evidence is identified in the source notes.',48,594,870,11,'berry')
end()
# 04
start('04 / Creative direction','ink')
text('Pink energy.',48,110,79,'Display','cream');text('Blue attitude.',48,199,79,'Italic','sky-blue')
rect(605,104,347,390,'blush',32);heart(712,208,132,'pink',True)
line(647,385,910,385,'deep-blue',2);text('THE MOOD',647,416,11,'Bold','ink');para('Bubblegum pink. Sky blue.\nA flash of hot pink.',647,443,260,17,'ink','Display')
para('Beauty-editorial typography meets the saturated pink-and-blue energy of the supplied brand reference. Spacious layouts, a single playful symbol, and confident copy make the brand feel alluring and approachable.',50,371,470,19,'cream')
for i,s in enumerate(['FEMININE','FLIRTATIOUS','POLISHED','LOCAL']):text(s,50+i*227,575,12,'Bold','blush')
end('ink')
# 05
start('05 / Logo suite');title('THE SIGNATURE','A name with a little curve.','Proposed typographic wordmark: Cormorant Garamond Semibold Italic. This is new concept artwork.')
rect(48,227,565,326,'blush',16);word(79,314,115,'pink');label('PORTLAND BIKINI COFFEE',198,445,'ink')
rect(637,227,315,151,'deep-blue',16);word(680,268,64,'cream');label('REVERSED WORDMARK',660,351,'cream')
rect(637,402,151,151,'pink',16);heart(678,438,70,'cream',False)
rect(812,402,140,151,'sky-blue',16);heart(847,438,70,'deep-blue',True)
para('Primary / wordmark + optional factual descriptor',48,578,550,12,'berry')
para('Heart / social avatar     Bean-heart / accent',637,578,315,11,'berry')
end()
# 06
start('06 / Logo use');title('GIVE IT ROOM','Consistency makes it recognizable.')
rect(48,225,570,275,'blush',10)
for x in [85,580]:line(x,258,x,461,'berry',.6)
for y in [258,461]:line(85,y,580,y,'berry',.6)
word(124,312,107,'pink');text('x',63,350,17,'Italic','berry');text('x',330,237,17,'Italic','berry')
para('Clear space = at least the lowercase “a” height at the chosen logo size. Keep type, photos, and edges outside this area.',48,525,560,14,'berry')
bullet('01','Minimum size','Wordmark: 140 px digital / 35 mm print. Symbol: 24 px / 6 mm. Use the plain heart below 32 px.',664,229,275)
bullet('02','Approved color','Magenta or deep blue on paper; navy on bubblegum/sky. Paper on magenta/navy. One solid color per mark.',664,375,275)
para('Keep the proportions and letter spacing supplied. Avoid outlines, shadows, gradients, rotation, or placing the mark over busy photos. Logo artwork is a concept; trademark clearance has not been performed.',48,595,900,11,'berry')
end()
# 07
start('07 / Color');title('THE CURRENT COLORWAY','Pink energy. Blue attitude.','Screen-derived from the supplied artwork. Paper, navy, and magenta are companion shades for readable layouts.')
sw=[('Paper','paper','Light canvas'),('Bubblegum','bubblegum','Pink surfaces'),('Hot pink','hot-pink','Vivid accents'),('Sky blue','sky-blue','Blue surfaces'),('Deep blue','deep-blue','Blue contrast'),('Magenta','magenta','Text / actions'),('Navy','navy','Primary type')]
for i,(n,k,d) in enumerate(sw):
 x=48+i*130;rect(x,242,122,190,k,10);text(n,x,452,18,'Display');text(C[k],x,483,10,'Bold');para(d,x,513,120,10,'berry')
line(48,561,952,561)
def lum(h):
 v=[int(h[i:i+2],16)/255 for i in (1,3,5)];v=[z/12.92 if z<=.04045 else ((z+.055)/1.055)**2.4 for z in v];return .2126*v[0]+.7152*v[1]+.0722*v[2]
def ratio(a,b):
 a,b=sorted([lum(C[a]),lum(C[b])]);return (b+.05)/(a+.05)
text('TEXT PAIRINGS',48,584,10,'Bold','pink')
for i,(a,b) in enumerate([('navy','paper'),('muted','paper'),('paper','magenta')]):text(f'{a.title()} / {b.title()}  {ratio(a,b):.1f}:1',225+i*240,583,12,'Bold')
para('Hot pink and sky blue are accents, not small white-text backgrounds. Use navy on bubblegum or sky; paper on magenta or deep blue.',48,615,900,11,'berry')
end()
# 08
start('08 / Typography');title('THE TYPE SYSTEM','Expressive up top. Clear everywhere.')
text('Cormorant',48,225,78,'Display');text('Garamond',48,298,78,'Italic','pink')
text('Aa Bb Cc & 0123456789',51,405,28,'Display');para('Semibold 600 + Semibold Italic 600\nHeadlines, wordmark, and short editorial statements.',51,454,445,14,'berry')
rect(568,227,384,328,'blush',14);text('DM Sans',599,260,43,'Bold');para('Espresso. Smoothies.\nEnergy spritzers.',600,326,305,21);para('Regular 400 for body text. Semibold 600 for navigation, labels, and buttons.',600,432,302,14,'berry')
line(48,573,952,573)
para('WEB SCALE: 72/76 hero • 48/52 section • 24/30 subhead • 18/28 body • 14/20 label. Mobile: 48/50 hero, 36/40 section. Keep paragraphs under 65 characters per line.',48,594,895,12,'berry')
end()
# 09
start('09 / Graphic language');title('THE SMALL DETAILS','A wink, not a wall of decoration.')
rect(48,230,270,280,'pink',14);heart(121,283,120,'cream',True);text('THE BEAN-HEART',71,464,11,'Bold','cream')
rect(341,230,283,280,'blush',14)
for yy in range(260,440,65):
 for xx in range(370,590,65):heart(xx,yy,23,'pink',False)
text('THE SPARSE REPEAT',363,464,11,'Bold')
rect(647,230,305,280,'deep-blue',14)
line(678,289,920,289,'blush');text('a little',686,318,52,'Italic','cream');text('mischief.',686,373,52,'Italic','cream');line(678,445,920,445,'blush')
for x,h,b in [(48,'Heart + coffee','A heart with a curved coffee-bean seam. Use as an accent or avatar.'),(341,'Repeat with restraint','Best on tissue, sleeve backs, and social backgrounds. Keep text areas quiet.'),(647,'Rules + curves','Thin dividers, capsule labels, and generous curves provide structure.')]:
 text(h,x,537,22,'Display');para(b,x,576,270,12,'berry')
end()
# 10
start('10 / Voice');title('HOW BAERISTAS SOUNDS','Warm. Confident. A little cheeky.','Speak as a welcoming host with personality. Keep the invitation playful and practical information plain.')
rect(48,229,545,264,'blush',14)
label('PROPOSED CAMPAIGN LINE',74,256);text('A little morning',74,305,52,'Display');text('mischief.',74,362,59,'Italic','pink')
text('SECONDARY COPY',637,238,10,'Bold','pink')
for yy,h,b in [(277,'Your daily dose of pink.','Hero / campaign headline'),(353,'Pull up. Perk up.','Drive-through social caption'),(429,'Find your stand.','Primary website action')]:text(h,637,yy,28,'Display');text(b,639,yy+37,12,'Body','berry')
line(48,530,952,530)
para('A useful introduction',48,553,220,14,'pink','Bold');para('Meet Baeristas: a woman-owned bikini coffee stop in Portland. Espresso, smoothies, and energy spritzers, served with personality.',299,550,650,17)
para('Avoid invented founder stories, claims about employees’ past careers, exclusivity claims, or unconfirmed menu promises. Let the team choose how it is represented.',48,617,900,10,'berry')
end()
# 11
start('11 / Photography');title('THE ART DIRECTION','Attraction through atmosphere.','The photograph should make you want the drink and feel welcome at the window.')
for x,bg,k,h,b in [(48,'blush','01 / PRODUCT','Close. Tactile. Delicious.','Approved drinks photographed close up: condensation, light, and texture. Pink, blue, or paper backdrops.'),(360,'pink','02 / SERVICE','Confident. Human. Warm.','Adult staff, with explicit approval for each use. Eye-level framing, chosen styling, natural interaction.'),(672,'ink','03 / PLACE','Local. Real. Recognizable.','Actual stand exteriors and service windows. Include approach views that help people recognize the stop.')]:
 rect(x,234,280,100,bg,12);text(k,x+23,271,11,'Bold','cream' if bg!='blush' else 'ink');text(h,x,362,23,'Display');para(b,x,407,273,15,'berry')
line(48,545,952,545)
para('Shoot list: one hero drink, one image per confirmed drink category, two stand exteriors, one service-window interaction, and one branded-cup detail. Capture 4:5, square, and wide crops.',48,565,880,14)
para('No staff or storefront images are fabricated in this kit. All application art is original vector concept artwork; photographed subjects and branded production assets still need to be supplied.',48,618,890,10,'berry')
end()
# 12
start('12 / Packaging concepts','blush');label('BRAND IN THE HAND',48,91);text('Good taste.',48,127,70,'Display');text('Great company.',48,199,70,'Italic','pink')
cup(290,342,1.03,'cream','pink');cup(720,245,1.28,'cream','deep-blue')
label('01 / MAGENTA SLEEVE',65,592);label('02 / DEEP BLUE SLEEVE',630,592)
para('Illustrated cup studies / proposed applications. Dimensions, substrates, and ink separations require supplier proofs.',48,622,904,10,'berry')
end()
# 13
start('13 / Social templates');title('BUILT FOR THE FEED','Recognizable in a single scroll.','A coordinated system for announcements, drink features, and visits. These examples use original illustration.')
for x,bg in [(48,'pink'),(360,'blush'),(672,'deep-blue')]:rect(x,239,280,280,bg,12)
word(70,258,40,'cream');text('Pull up.',72,334,48,'Display','cream');text('Perk up.',72,385,48,'Italic','cream');heart(251,456,40,'cream')
label('COFFEE WITH PERSONALITY',383,265);cup(501,316,.62,'cream','pink');word(391,463,53,'pink')
label('PORTLAND, OREGON',696,264,'blush');text('Find your',695,330,43,'Display','cream');text('Baeristas.',695,379,43,'Italic','blush');text('Drive-through coffee.',697,468,14,'Body','cream')
for x,h,b in [(48,'01 / Brand moment','One short thought. Large type. One symbol.'),(360,'02 / Drink feature','Replace illustration with approved drink photography.'),(672,'03 / Visit prompt','Add confirmed stand details in the caption.')]:text(h,x,545,22,'Display');para(b,x,582,270,12,'berry')
end()
# 14
start('14 / Digital direction');title('BRAND TO BROWSER','The next expression: the website.','Design handoff principles for the separate website mockup.')
rect(48,225,566,369,'blush',16);word(76,250,47,'pink');line(76,310,585,310,'pink',.5)
text('Your daily',76,343,48,'Display');text('dose of pink.',76,394,49,'Italic','pink');rect(76,470,157,40,'pink',20);text('Find your stand',154,483,12,'Bold','cream','center');heart(450,363,90,'pink',True)
text('Espresso / Smoothies / Energy spritzers',78,555,12,'Body','berry')
bullet('01','Make the visit easy','Lead with the brand, drink categories, and directions. Design the mobile visit path first.',658,232,280)
bullet('02','Keep the personality','Large serif headlines, vivid pink-and-blue surfaces, confident copy, and real business photography.',658,373,280)
para('The small composition at left is a visual system study, not a completed website. The next phase expands this into desktop and mobile layouts.',658,540,275,12,'berry')
end()
# 15
start('15 / Handoff');title('READY TO USE, READY TO REFINE','A practical kit for the next phase.')
items=[('INCLUDED','PDF brand guide; outlined SVG wordmarks; heart and bean-heart marks; SVG pattern; color tokens; licensed font files; editable PDF-generation source.'),('OWNER CONFIRMATIONS','Preferred full brand name, existing logo files or guidelines, current vegan/menu claims, both locations and hours, social handle, approved staff and drink photography.'),('PRODUCTION NOTES','Digital colors are defined in sRGB. Ask the printer for substrate-specific CMYK conversions and a physical proof. Cup drawings are concept mockups, not dielines.'),('NEXT / WEBSITE MOCKUP','Apply this system to responsive desktop and mobile layouts. Use directions as the primary action; expose menu, social, and ordering links only when verified.')]
for i,(h,b) in enumerate(items):
 y=232+i*94;line(48,y-15,952,y-15);label(h,48,y);para(b,336,y,605,14)
end()
# 16
start('16 / Sources & provenance');title('RESEARCH CHECKED / OCTOBER 29, 2026','Evidence, with its limits.')
sources=[('S1 / NOV 2025 BUSINESS AD','Published ad / search-indexed text + visual description. Historical green identity and brand positioning.','https://www.exoticunderground.com/pdf/33-05-nov25/3305_exotic_main_WEB.pdf'),('S2 / DEC 2025 BUSINESS AD','Published ad / search-indexed text. Drive-through drink categories, woman-owned positioning, NW address.','https://www.exoticmonthly.com/pdf/33-06-dec25/3306_exotic_main_WEB.pdf'),('S3 / JAN 2026 BUSINESS AD','Published ad / search-indexed text. Reinforces vegan bikini-coffee positioning; historical hours.','https://xmag.com/pdf/33-07-jan26/3307_exotic_main_WEB.pdf'),('S4 / INDEXED BUSINESS SOCIAL PROFILE','Secondary mirror of business posts and bio. Pink self-description and two reported addresses. Direct X/Instagram access limited.','https://mobile.twstalker.com/BaeristasPDX'),('S5 / JOE DIRECTORY','Indexed directory / direct fetch returned 403. Corroborates NW address. Current operating details remain unconfirmed.','https://joe.coffee/locations/or/portland/baeristas-vegan-espresso-portland/'),('S6 / LOCAL CATEGORY REFERENCE','Competitor first-party website. Reviewed for category context; no assets or wording reused.','https://topoffespresso.com/')]
y=207
for h,b,url in sources:
 label(h,48,y);para(b,48,y+19,865,10,'berry',leading=13);text('OPEN SOURCE ↗',952,y,9,'Bold','pink','right');c.linkURL(url,(849,H-y-14,954,H-y+2),relative=0);y+=64
para('Original concept artwork throughout. Fonts: Cormorant Garamond and DM Sans, distributed under the SIL Open Font License; license copies included. Current colorway supplied by the user (REF). No third-party business photography republished. Research log contains access notes and unresolved facts.',48,604,900,10,'berry',leading=14)
end()
c.save()
print(ROOT/'Baeristas_Brand_Kit.pdf')
