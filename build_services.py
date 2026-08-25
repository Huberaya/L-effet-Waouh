#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Instantané autonome de la page Services (carrousels avec images base64)."""
import base64, io, os, html
from PIL import Image

VIS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visuels")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "waouh", "site", "services.html")

SERVS = [
    ("Photobooth 360", "Vidéos slow-motion 360° partagées en QR code. L'effet foule garanti, l'animation star des Reels.", 550, "6 h, opérateur inclus",
     ["02-photobooth-360.jpg", "01-hero.jpg", "09-premiere-danse.jpg", "12-installation.jpg"]),
    ("Miroir magique", "Miroir à selfie tactile : impressions, animations, messages. Le premium du photobooth.", 600, "la soirée",
     ["07-miroir-magique.jpg", "07-miroir-magique-v1.jpg", "07-miroir-magique-v2.jpg", "07-miroir-magique-v3.jpg"]),
    ("Livre d'or audio", "Téléphone vintage : vos invités laissent un message vocal. Le gadget viral 2026.", 99, "le week-end",
     ["03-livre-or-audio.jpg", "10-vin-honneur.jpg", "03-livre-or-audio-v1.jpg", "10-vin-honneur-v1.jpg"]),
    ("Néon « Mr & Mrs »", "Enseigne LED personnalisée : le fond de photo de toutes vos soirées.", 150, "le week-end",
     ["04-neon.jpg", "01-hero.jpg", "10-vin-honneur.jpg", "04-neon-v1.jpg"]),
    ("Lettres géantes « LOVE »", "Décor lumineux iconique, le coin photo qui attire tout le monde.", 250, "le week-end",
     ["04-neon-v2.jpg", "01-hero-v1.jpg", "10-vin-honneur-v2.jpg", "04-neon-v3.jpg"]),
    ("Cierges magiques", "Le tunnel d'étincelles de fin de soirée. La photo iconique du mariage.", 180, "le soir (extérieur)",
     ["05-cierges-magiques.jpg", "05-cierges-magiques-v1.jpg", "05-cierges-magiques-v2.jpg", "05-cierges-magiques-v3.jpg"]),
    ("Bulles & confettis", "La sortie de mairie effet cinéma : nuage de bulles et pluie de confettis.", 150, "la sortie de mairie",
     ["06-bulles-confettis.jpg", "06-bulles-confettis-v1.jpg", "06-bulles-confettis-v2.jpg", "06-bulles-confettis-v3.jpg"]),
    ("Canons à confettis CO2", "Explosion de couleurs synchronisée pour la première danse.", 250, "la première danse",
     ["09-premiere-danse.jpg", "09-premiere-danse-v1.jpg", "09-premiere-danse-v2.jpg", "09-premiere-danse-v3.jpg"]),
    ("Piscine à balles LED", "Le coin lounge lumineux qui fait le tour des Reels. Carton garanti.", 300, "la soirée",
     ["08-piscine-balles.jpg", "08-piscine-balles-v1.jpg", "08-piscine-balles-v2.jpg", "08-piscine-balles-v3.jpg"]),
]

def datauri(name, max_w=820, q=76):
    p = os.path.join(VIS, name)
    im = Image.open(p).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

cards = ""
for name, desc, prix, unit, imgs in SERVS:
    slides = "".join(f'<img src="{datauri(f)}" alt="{html.escape(name)}">' for f in imgs)
    cards += f'''<div class="serv">
<div class="carousel"><div class="track">{slides}</div>
<span class="counter">1/{len(imgs)}</span>
<button class="navbtn prev">‹</button><button class="navbtn next">›</button>
<div class="dots"></div>
</div>
<div class="sinfo"><h3>{html.escape(name)}</h3><p>{html.escape(desc)}</p>
<div class="prix">{prix} € <small>/ {html.escape(unit)}</small></div>
<a class="btn small" href="/reservation">Réserver cette animation</a>
</div></div>'''

CSS = """
:root{--cream:#FAF6F0;--ink:#2F2A25;--terra:#B0764A;--terra2:#C67B4F;--gold:#D9A441;--gold2:#E8B26A;--sage:#7A8B6F;--line:#E7DED2;--soft:#F3EAE0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;background:var(--cream);color:var(--ink);line-height:1.6}
.wrap{max-width:1080px;margin:0 auto;padding:0 22px}
h1,h2,h3{font-family:Georgia,'Times New Roman',serif;line-height:1.15}
.topbar{position:sticky;top:0;z-index:100;background:rgba(250,246,240,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.topbar .in{max-width:1080px;margin:0 auto;padding:12px 22px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.brand{font-family:Georgia,serif;font-weight:700;font-size:20px;color:var(--ink)}
.brand .spark{color:var(--gold)}
.brand small{display:block;font-family:-apple-system,sans-serif;font-size:9.5px;letter-spacing:2.2px;color:var(--terra);font-weight:700;text-transform:uppercase}
.pagehero{background:linear-gradient(150deg,#2F2A25 0%,#4a3a2c 60%,#6b4a2f 100%);color:#fff;padding:56px 0 48px;text-align:center}
.pagehero .kick{display:inline-block;color:#E8B26A;font-size:11px;letter-spacing:2.5px;text-transform:uppercase;font-weight:700;margin-bottom:10px}
.pagehero h1{font-size:clamp(30px,4.5vw,46px);margin-bottom:10px}
.pagehero p{color:#efe3d2;max-width:620px;margin:0 auto;font-size:16px}
section{padding:60px 0}
.center{text-align:center}
.center .sub{margin-left:auto;margin-right:auto}
.sub{color:#6b5f52;max-width:660px;margin-bottom:28px;font-size:16px}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.serv{background:#fff;border:1px solid var(--line);border-radius:20px;overflow:hidden;box-shadow:0 8px 28px rgba(47,42,37,.07);display:flex;flex-direction:column}
.carousel{position:relative;aspect-ratio:4/3;overflow:hidden;background:#1d150e}
.carousel .track{display:flex;height:100%;transition:transform .45s ease}
.carousel .track img{width:100%;height:100%;object-fit:cover;flex:0 0 100%;display:block}
.carousel .navbtn{position:absolute;top:50%;transform:translateY(-50%);width:36px;height:36px;border-radius:50%;background:rgba(24,15,10,.55);border:1px solid rgba(255,255,255,.4);color:#fff;font-size:17px;cursor:pointer;z-index:3;line-height:1;display:flex;align-items:center;justify-content:center}
.carousel .navbtn:hover{background:rgba(24,15,10,.8)}
.carousel .prev{left:10px}.carousel .next{right:10px}
.carousel .dots{position:absolute;bottom:10px;left:0;right:0;display:flex;gap:6px;justify-content:center;z-index:3}
.carousel .dots span{width:8px;height:8px;border-radius:50%;background:rgba(255,255,255,.45);cursor:pointer}
.carousel .dots span.on{background:var(--gold)}
.carousel .counter{position:absolute;top:10px;right:12px;z-index:3;background:rgba(24,15,10,.6);color:#fff;font-size:11px;font-weight:700;padding:3px 9px;border-radius:999px}
.serv .sinfo{padding:20px 22px;flex:1;display:flex;flex-direction:column}
.serv .sinfo h3{font-size:20px;margin-bottom:6px}
.serv .sinfo p{color:#5c5246;font-size:14px;flex:1}
.serv .sinfo .prix{font-family:Georgia,serif;font-size:22px;color:var(--terra);margin-top:10px}
.serv .sinfo .prix small{font-size:13px;font-family:system-ui;color:#6b5f52}
.serv .sinfo .cta{margin-top:12px}
.btn{display:inline-block;background:var(--terra);color:#fff;padding:12px 22px;border-radius:999px;font-weight:700;font-size:15px;border:1px solid var(--terra);cursor:pointer;transition:.15s;text-decoration:none}
.btn:hover{background:var(--terra2);border-color:var(--terra2);transform:translateY(-1px)}
.btn.gold{background:var(--gold);border-color:var(--gold)}
.btn.small{padding:8px 16px;font-size:13.5px}
.note{text-align:center;color:#9b8f80;font-size:12.5px;margin-top:22px}
@media(max-width:820px){.grid3{grid-template-columns:1fr}}
"""

html_doc = f"""<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Nos animations — L'Effet Waouh</title>
<style>{CSS}</style></head><body>
<div class="topbar"><div class="in"><a href="#" class="brand"><span class="spark">✦</span> L'Effet Waouh<small>Animations &amp; gadgets de mariage</small></a></div></div>
<div class="pagehero"><div class="wrap"><span class="kick">✦ L'Effet Waouh · Animations de mariage</span>
<h1>Nos animations &amp; gadgets</h1>
<p>Tout se loue à la journée, livré et installé (opérateur inclus dans les packs). Faites défiler les photos de chaque animation.</p></div></div>
<section><div class="wrap">
<div class="grid3">{cards}</div>
<p class="note">Photos d'illustration (visuels de démonstration) — remplacées par nos photos réelles de prestations.</p>
</div></section>
<script>
document.querySelectorAll('.carousel').forEach(function(c){{
  var track=c.querySelector('.track'), slides=track.children, n=slides.length, i=0, t=null;
  var dots=c.querySelector('.dots'), counter=c.querySelector('.counter');
  for(var k=0;k<n;k++){{var d=document.createElement('span'); if(k===0)d.className='on'; (function(k){{d.onclick=function(){{go(k)}}}})(k); dots.appendChild(d);}}
  function go(x){{i=((x%n)+n)%n; track.style.transform='translateX(-'+(i*100)+'%)';
    dots.querySelectorAll('span').forEach(function(dd,j){{dd.classList.toggle('on',j===i)}});
    if(counter) counter.textContent=(i+1)+'/'+n;}}
  c.querySelector('.next').onclick=function(){{go(i+1)}};
  c.querySelector('.prev').onclick=function(){{go(i-1)}};
  function play(){{clearInterval(t); t=setInterval(function(){{go(i+1)}},3600)}};
  c.addEventListener('mouseenter',function(){{clearInterval(t)}});
  c.addEventListener('mouseleave',play);
  play();
}});
</script>
</body></html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html_doc)
print("OK ->", OUT, f"{os.path.getsize(OUT)/1024:.0f} Ko")
