"""Refresh visual review assets and downloadable packages after PDF/browser rendering."""
from pathlib import Path
import shutil, zipfile
from PIL import Image
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[2]
DOCS=['README.md','RESEARCH.md','ASSETS.md','OWNER_CHECKLIST.md','VALIDATION.md']
pdf=ROOT/'branding/Baeristas_Brand_Kit.pdf'
p=fitz.open(pdf)
contact=Image.new('RGB',(2000,350*((len(p)+3)//4)),'white')
for obsolete in (ROOT/'branding/previews').glob('page-*.png'):
 obsolete.unlink()
for i,page in enumerate(p):
 pix=page.get_pixmap(matrix=fitz.Matrix(.5,.5),alpha=False)
 im=Image.frombytes('RGB',[pix.width,pix.height],pix.samples)
 im.save(ROOT/f'branding/previews/page-{i+1:02}.png')
 contact.paste(im,((i%4)*500,(i//4)*350))
contact.save(ROOT/'branding/previews/contact-sheet.jpg')
for width in [390,768,1440]:
 im=Image.open(ROOT/f'website-mockup/previews/{width}.png')
 im.thumbnail((900,2700));im.save(ROOT/f'website-mockup/previews/{width}-review.png')
out=ROOT/'deliverables';out.mkdir(exist_ok=True)
shutil.copy2(pdf,out/'Baeristas_Brand_Kit_Current_Colorway.pdf')
with zipfile.ZipFile(out/'Baeristas_Review_Package_Current_Colorway.zip','w',zipfile.ZIP_DEFLATED) as z:
 for folder in ['branding','website-mockup','scripts']:
  for file in (ROOT/folder).rglob('*'):
   if file.is_file():z.write(file,file.relative_to(ROOT))
 for file in DOCS:z.write(ROOT/file,file)
shutil.copy2(out/'Baeristas_Review_Package_Current_Colorway.zip',out/'Baeristas_Review_Package.zip')
with zipfile.ZipFile(out/'Baeristas_Website_Current_Colorway.zip','w',zipfile.ZIP_DEFLATED) as z:
 for file in (ROOT/'website-mockup').rglob('*'):
  if file.is_file():z.write(file,file.relative_to(ROOT/'website-mockup'))
 z.write(ROOT/'ASSETS.md','ASSETS.md')
shutil.copy2(out/'Baeristas_Brand_Kit_Current_Colorway.pdf',out/'Baeristas_Brand_Kit_Y2K.pdf')
shutil.copy2(out/'Baeristas_Review_Package_Current_Colorway.zip',out/'Baeristas_Review_Package_Y2K.zip')
shutil.copy2(out/'Baeristas_Website_Current_Colorway.zip',out/'Baeristas_Website_Y2K.zip')
print('Y2K PDF, previews, full review ZIP and standalone website ZIP refreshed.')
