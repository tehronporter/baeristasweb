"""Copy the review website's public files into GitHub Pages' /docs source."""
from pathlib import Path
import shutil
root=Path(__file__).resolve().parents[1]
source=root/'website-mockup'
dest=root/'docs'
dest.mkdir(exist_ok=True)
for name in ['index.html','style.css','script.js']:
 shutil.copy2(source/name,dest/name)
assets=dest/'assets';assets.mkdir(exist_ok=True)
for file in (source/'assets').iterdir():
 if file.suffix in ['.svg','.ttf','.txt']:
  shutil.copy2(file,assets/file.name)
(dest/'.nojekyll').touch()
print('Prepared docs/ for GitHub Pages.')
