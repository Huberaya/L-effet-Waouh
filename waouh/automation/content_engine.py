#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moteur de contenu — L'Effet Waouh.
Recycle une idée en : 1 article de blog → 1 newsletter → 1 script Reel →
3 scripts TikTok → 1 carrousel → 5 Stories.
Usage : python3 automation/content_engine.py
Lit content/topics.json, écrit dans content/generated/<slug>/.
"""
import os, json, datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS = os.path.join(BASE, "content", "topics.json")
OUT = os.path.join(BASE, "content", "generated")
os.makedirs(OUT, exist_ok=True)

def slugify(s):
    return "".join(c if c.isalnum() else "-" for c in s.lower()).strip("-")

def generate(t):
    slug = t["slug"]; titre = t["titre"]; angle = t["angle"]
    d = os.path.join(OUT, slug); os.makedirs(d, exist_ok=True)

    article = f"""# {titre}

{angle}. Dans cet article, nous faisons le point sur les bonnes pratiques, les prix et les erreurs à éviter.

## Pourquoi c'est important
Le jour J, l'animation représente une petite part du budget mais la majorité des souvenirs. Bien la choisir, c'est garantir des invités émerveillés et des centaines de photos partagées.

## Nos conseils
- Privilégier 2 à 3 animations bien placées plutôt que 10 gadgets.
- Toujours prévoir un opérateur pour coordonner.
- Anticiper le plan B météo.

## Les prix
Comptez de 150 € (sortie de mairie) à 1 500 € (pack complet) selon le niveau d'ambition.

## Conclusion
L'effet waouh ne dépend pas du budget mais du bon choix d'animations, au bon moment, avec la bonne logistique. L'Effet Waouh s'occupe de tout.

*Article généré par le moteur de contenu — à enrichir et relire avant publication.*
"""
    newsletter = f"""Objet : {titre}

Bonjour,

{angle}.

Chez L'Effet Waouh, on loue les animations qui rendent un mariage inoubliable : photobooth 360, livre d'or audio, néons, cierges magiques — livrés et opérés.

➡️ Réservez votre date : leffetwaouh.fr

À très vite,
L'Effet Waouh
"""
    reel = f"""REEL — {titre}
Hook (0-3 s) : « {angle} ? Voici ce que personne ne te dit. »
Script : démo en 3 plans (problème → solution → résultat), texte à l'écran, musique tendance.
CTA : « Lien en bio » / « DM le mot-clé ».
"""
    tiktoks = "\n\n".join([
        f"TIKTOK 1 — {titre} : hook choc + démo 15 s (objectif : portée).",
        f"TIKTOK 2 — {titre} : 3 idées concrètes en liste (objectif : sauvegarde).",
        f"TIKTOK 3 — {titre} : « ne fais pas ça » / erreur fréquente (objectif : commentaires).",
    ])
    carrousel = f"""CARROUSEL — {titre}
Slide 1 : hook ({angle}). Slide 2-4 : 3 conseils chiffrés. Slide 5 : CTA.
"""
    stories = "\n".join([
        "STORY 1 : sondage « plutôt A ou B ? »",
        "STORY 2 : question ouverte sur le sujet",
        "STORY 3 : rappel du lien en bio",
        "STORY 4 : avis/testimonial à insérer",
        "STORY 5 : compte à rebours / urgence",
    ])

    files = {"article.md": article, "newsletter.md": newsletter, "reel.md": reel,
             "tiktoks.md": tiktoks, "carrousel.md": carrousel, "stories.md": stories}
    for fn, content in files.items():
        with open(os.path.join(d, fn), "w", encoding="utf-8") as f:
            f.write(content)
    return d

if __name__ == "__main__":
    topics = json.load(open(TOPICS, encoding="utf-8"))
    for t in topics:
        generate(t)
    print(f"✅ {len(topics)} sujets déployés dans {OUT}")
