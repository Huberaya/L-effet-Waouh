#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit le catalogue visuel HTML avec images intégrées en base64."""
import base64, io, os
from PIL import Image

VISUELS = "visuels"
OUT = "catalogue-visuel.html"

def img_to_datauri(path, max_w=900, quality=80):
    im = Image.open(path).convert("RGB")
    if im.width > max_w:
        h = int(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, format="JPEG", quality=quality, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def datauri(name):
    return img_to_datauri(os.path.join(VISUELS, name))

hero = datauri("01-hero.jpg")

cards = [
    {
        "img": datauri("02-photobooth-360.jpg"),
        "tag": "L'attraction star",
        "trend": "Tendance TikTok #1",
        "title": "Photobooth 360",
        "desc": "Plateforme LED + bras caméra, vidéos slow-motion partagées en QR code. Effet foule garanti, idéal première danse.",
        "achat": "Achat : 2 400 – 3 300 €",
        "loc": "Location : 550 – 950 €",
        "amorti": "Amorti en 5-6 locations",
    },
    {
        "img": datauri("03-livre-or-audio.jpg"),
        "tag": "Le gadget viral",
        "trend": "Tendance TikTok #2",
        "title": "Livre d'or audio",
        "desc": "Téléphone vintage qui enregistre les messages vocaux des invités. Émotion + nostalgie, la star de 2026.",
        "achat": "Achat : ~150 € (DIY)",
        "loc": "Location : 89 – 180 €",
        "amorti": "Amorti en 1-2 locations",
    },
    {
        "img": datauri("04-neon.jpg"),
        "tag": "Fond de photo",
        "trend": "Vu sur tous les Reels",
        "title": "Néon « Mr & Mrs »",
        "desc": "Enseigne LED personnalisée, se retrouve sur toutes les photos des invités. Louez les modèles génériques.",
        "achat": "Achat : 60 – 300 €",
        "loc": "Location : 150 – 350 €",
        "amorti": "Amorti en 1-2 locations",
    },
    {
        "img": datauri("05-cierges-magiques.jpg"),
        "tag": "La photo iconique",
        "trend": "Sparkler exit",
        "title": "Cierges magiques",
        "desc": "Tunnel d'étincelles en fin de soirée, la photo la plus partagée du mariage. Consommable à forte marge.",
        "achat": "Achat : < 1 € / pièce",
        "loc": "Location : 150 – 300 € le pack",
        "amorti": "Rentable dès la 1re fois",
    },
    {
        "img": datauri("06-bulles-confettis.jpg"),
        "tag": "Sortie de mairie",
        "trend": "Effet cinéma à 40 €",
        "title": "Bulles & confettis",
        "desc": "Machines à bulles, canons à confettis CO2 et fumée pour la sortie de mairie et la première danse.",
        "achat": "Achat : 40 – 400 €",
        "loc": "Location : 150 – 450 €",
        "amorti": "Amorti en 1-2 prestations",
    },
    {
        "img": datauri("07-miroir-magique.jpg"),
        "tag": "Le premium",
        "trend": "Gros ticket",
        "title": "Miroir magique",
        "desc": "Miroir à selfie avec écran tactile, impressions et animations. Se loue cher, se démarque du photobooth.",
        "achat": "Achat : 3 000 – 5 000 €",
        "loc": "Location : 600 – 750 €",
        "amorti": "Amorti en 5-7 locations",
    },
    {
        "img": datauri("08-piscine-balles.jpg"),
        "tag": "Le coin instagrammable",
        "trend": "Effet wow déco",
        "title": "Piscine à balles LED",
        "desc": "Coin lounge lumineux pour la soirée, se loue en complément du photobooth. Carton garanti en Reels.",
        "achat": "Achat : 500 – 1 000 €",
        "loc": "Location : 250 – 400 €",
        "amorti": "Amorti en 2-4 locations",
    },
]

cards_html = ""
for c in cards:
    cards_html += f"""
    <div class="card">
      <div class="imgwrap"><img src="{c['img']}" alt="{c['title']}"></div>
      <div class="body">
        <div class="badges">
          <span class="trend">{c['trend']}</span>
        </div>
        <h3>{c['title']}</h3>
        <p class="tagline">{c['tag']}</p>
        <p class="desc">{c['desc']}</p>
        <div class="prices">
          <span class="pill achat">{c['achat']}</span>
          <span class="pill loc">{c['loc']}</span>
        </div>
        <div class="amorti">{c['amorti']}</div>
      </div>
    </div>"""

html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Catalogue visuel — Location de matériel & gadgets de mariage</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    background: #faf6f0; color: #2f2a25; line-height: 1.5;
  }}
  .wrap {{ max-width: 1080px; margin: 0 auto; padding: 40px 20px 60px; }}
  header {{ text-align: center; margin-bottom: 32px; }}
  header .kicker {{
    display: inline-block; letter-spacing: 3px; text-transform: uppercase;
    font-size: 12px; color: #b0764a; font-weight: 700; margin-bottom: 10px;
  }}
  header h1 {{
    font-family: Georgia, 'Times New Roman', serif; font-size: 40px; line-height: 1.15;
    font-weight: 700; color: #2f2a25; margin-bottom: 10px;
  }}
  header h1 em {{ color: #b0764a; font-style: italic; }}
  header p.sub {{ color: #6b5f52; font-size: 17px; max-width: 640px; margin: 0 auto; }}
  .hero {{
    position: relative; border-radius: 20px; overflow: hidden; margin-bottom: 40px;
    box-shadow: 0 20px 50px rgba(47,42,37,.18);
  }}
  .hero img {{ width: 100%; display: block; }}
  .hero .overlay {{
    position: absolute; inset: 0;
    background: linear-gradient(180deg, rgba(20,15,10,0) 30%, rgba(20,15,10,.72) 100%);
    display: flex; flex-direction: column; justify-content: flex-end; padding: 28px;
  }}
  .hero .overlay h2 {{
    font-family: Georgia, serif; color: #fff; font-size: 28px; margin-bottom: 6px;
  }}
  .hero .overlay p {{ color: #f3e9dd; font-size: 15px; max-width: 560px; }}
  .grid {{
    display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px;
  }}
  .card {{
    background: #fff; border-radius: 18px; overflow: hidden;
    box-shadow: 0 8px 26px rgba(47,42,37,.08); display: flex; flex-direction: column;
    transition: transform .18s ease, box-shadow .18s ease;
  }}
  .card:hover {{ transform: translateY(-4px); box-shadow: 0 16px 40px rgba(47,42,37,.14); }}
  .imgwrap {{ height: 220px; overflow: hidden; }}
  .imgwrap img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
  .body {{ padding: 18px; display: flex; flex-direction: column; gap: 8px; flex: 1; }}
  .trend {{
    display: inline-block; font-size: 11px; font-weight: 700; letter-spacing: .5px;
    text-transform: uppercase; color: #b0764a; background: #f6ece2;
    padding: 4px 10px; border-radius: 999px;
  }}
  h3 {{ font-family: Georgia, serif; font-size: 22px; color: #2f2a25; }}
  .tagline {{ font-size: 13px; color: #b0764a; font-weight: 600; }}
  .desc {{ font-size: 14px; color: #5c5246; }}
  .prices {{ display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px; }}
  .pill {{ font-size: 12.5px; font-weight: 600; padding: 6px 10px; border-radius: 999px; }}
  .achat {{ background: #e9f3ea; color: #2e7d43; }}
  .loc {{ background: #fdf1dd; color: #9a6a1f; }}
  .amorti {{ font-size: 12.5px; color: #8a7d6d; font-style: italic; margin-top: auto; padding-top: 6px; }}
  .strip {{
    margin-top: 40px; background: #2f2a25; color: #f3e9dd; border-radius: 18px;
    padding: 26px 28px; display: flex; flex-wrap: wrap; gap: 24px; align-items: center; justify-content: space-between;
  }}
  .strip h3 {{ font-family: Georgia, serif; font-size: 22px; color: #fff; }}
  .strip p {{ color: #cdc2b2; font-size: 14px; max-width: 560px; }}
  .strip .big {{ font-family: Georgia, serif; font-size: 34px; color: #e8b26a; white-space: nowrap; }}
  footer {{ text-align: center; color: #9b8f80; font-size: 12.5px; margin-top: 34px; }}
  @media (max-width: 820px) {{
    .grid {{ grid-template-columns: repeat(2, 1fr); }}
  }}
  @media (max-width: 540px) {{
    .grid {{ grid-template-columns: 1fr; }}
    header h1 {{ font-size: 30px; }}
  }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <span class="kicker">Catalogue visuel · 2026</span>
    <h1>Location de matériel &amp; gadgets <em>de mariage</em></h1>
    <p class="sub">Acheter malin, louer cher, rembourser vite — le catalogue illustré des animations qui font le buzz sur TikTok &amp; Instagram.</p>
  </header>

  <div class="hero">
    <img src="{hero}" alt="Réception de mariage avec photobooth 360 et néon Mr &amp; Mrs">
    <div class="overlay">
      <h2>Vos futurs best-sellers, en un seul parc de location</h2>
      <p>Un photobooth 360, un livre d'or audio, un néon : chaque objet se rembourse en 1 à 6 locations, puis génère ~90 % de marge à chaque mariage.</p>
    </div>
  </div>

  <div class="grid">
    {cards_html}
  </div>

  <div class="strip">
    <div>
      <h3>Pack de démarrage conseillé</h3>
      <p>Livre d'or audio + néon + photobooth open-air + bulles/fumée/confettis + cierges : un pack « mariage complet » se vend 800 à 1 200 €.</p>
    </div>
    <div class="big">~4 500 €</div>
  </div>

  <footer>Visuels d'illustration générés par IA — à remplacer par vos propres photos réelles pour Instagram/TikTok. · Dossier : business-location-materiel-mariage.md</footer>
</div>
</body>
</html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("OK ->", OUT, f"{os.path.getsize(OUT)/1024:.0f} Ko")
