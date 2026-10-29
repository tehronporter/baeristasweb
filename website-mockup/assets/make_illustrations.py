from pathlib import Path
A=Path(__file__).parent
svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 740" fill="none">
<defs><linearGradient id="bg" x2=".9" y2="1"><stop stop-color="#F7DCE4"/><stop offset="1" stop-color="#EAB2C4"/></linearGradient><linearGradient id="cup" x1=".1" x2="1"><stop stop-color="#FFF8F2"/><stop offset=".4" stop-color="#FFFDF9"/><stop offset="1" stop-color="#E8D2C6"/></linearGradient><linearGradient id="sleeve" x2="1"><stop stop-color="#B51F51"/><stop offset=".4" stop-color="#D13E71"/><stop offset="1" stop-color="#A81849"/></linearGradient><linearGradient id="lid" x2="1"><stop stop-color="#34201F"/><stop offset=".4" stop-color="#5A3B3B"/><stop offset="1" stop-color="#281514"/></linearGradient><filter id="shadow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="14"/></filter></defs>
<rect x="28" y="18" width="594" height="694" rx="280" fill="url(#bg)"/>
<ellipse cx="339" cy="614" rx="164" ry="25" fill="#8B405C" opacity=".2" filter="url(#shadow)"/>
<path d="M90 560C155 500 197 596 253 573" stroke="#FFF8F2" opacity=".6" stroke-width="2"/>
<g transform="translate(335 359) rotate(12)">
<path d="M-125-160H125L89 218Q0 249-89 218Z" fill="url(#cup)"/>
<path d="M-115-61H115L102 99Q0 126-102 99Z" fill="url(#sleeve)"/>
<rect x="-143" y="-177" width="286" height="30" rx="12" fill="url(#lid)"/>
<path d="M-119-178L-108-192H108L119-178" fill="url(#lid)"/>
<path d="M-128-165H128" stroke="#8D6966" stroke-width="2" opacity=".6"/>
<text x="0" y="28" font-family="Georgia,serif" font-size="47" font-style="italic" text-anchor="middle" fill="#FFF8F2">Baeristas</text>
<text x="0" y="56" font-family="Arial,sans-serif" font-size="7.7" letter-spacing="1.3" text-anchor="middle" fill="#FFF8F2">A LITTLE MORNING MISCHIEF.</text>
<path d="M-75 150Q-18 163 38 156" stroke="#E7CDD2" stroke-width="1"/>
</g>
<g transform="translate(487 139) rotate(12)"><path d="M22 41C13 33 0 22 0 12C0 0 15-4 22 6C30-4 44 0 44 12C44 22 30 33 22 41" fill="#C92E64"/></g>
<path d="M100 226V260M83 243H117" stroke="#C92E64" stroke-width="2"/><circle cx="511" cy="555" r="5" fill="#FFF8F2"/>
</svg>'''
(A/'hero-cup.svg').write_text(svg)
for kind,c1,c2 in [('espresso','#C59A79','#634132'),('smoothies','#EAA0B8','#CB567F'),('spritzers','#EDAD82','#D57580')]:
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 480"><defs><linearGradient id="drink" x2="0.7" y2="1"><stop stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient><linearGradient id="glass"><stop stop-color="#FFFFFF" stop-opacity=".6"/><stop offset=".4" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".3"/></linearGradient><filter id="s"><feGaussianBlur stdDeviation="9"/></filter></defs><ellipse cx="250" cy="410" rx="110" ry="17" fill="#7F4353" opacity=".15" filter="url(#s)"/><g transform="translate(250 230) rotate(-9)"><path d="M-87-129H87L67 158Q0 176-67 158Z" fill="url(#drink)"/><path d="M-87-129H87L67 158Q0 176-67 158Z" fill="url(#glass)" stroke="#FFF8F2" stroke-opacity=".6" stroke-width="2"/><ellipse cy="-128" rx="87" ry="15" fill="{c1}"/><rect x="-94" y="-143" width="188" height="19" rx="9" fill="#FFF8F2" fill-opacity=".75"/><path d="M27-136L49-224" stroke="#C92E64" stroke-width="10"/><path d="M-74-12H74L68 89Q0 106-68 89Z" fill="#FFF8F2"/><path d="M0 61C-10 53-31 40-31 25C-31 8-10 3 0 17C10 3 31 8 31 25C31 40 10 53 0 61" fill="#C92E64"/></g></svg>'''
 (A/f'{kind}.svg').write_text(s)
