from .base import BaseAgent
from datetime import datetime, timedelta

class SocialAgent(BaseAgent):
    """Publications réseaux"""
    def analyze(self):
        return {
            "trends": [
                "#genderreveal 5B vues TikTok",
                "#babyshower 10B",
                "#bapteme #anniversairelicorne",
                "Pinterest: 'gender reveal ideas' +320%"
            ],
            "accounts_needed": [
                "Instagram @leffetwaouh https://www.instagram.com/accounts/emailsignup/",
                "TikTok @leffetwaouh https://www.tiktok.com/signup",
                "Pinterest Business https://business.pinterest.com/",
                "Meta Business https://business.facebook.com/"
            ]
        }

    def recommend(self):
        return [
            "Reels 15s: démo ballon 90cm, tuto arche 85pcs, avant/après table mariage, fumigènes rose/bleu",
            "Carrousels: 5 idées déco mariage, 3 thèmes anniversaire 2024, checklist Baby Shower",
            "Stories: sondages Team Boy/Girl, coulisses Nantes, UGC clients",
            "Analyser tendances via web_search mais créer original sans copie illégale"
        ]

    def editorial_calendar_week(self):
        start = datetime.now()
        plan = [
            (start, "Reel", "Démo ballon 90cm éclatement", "TikTok/Insta", "Hook: 4409 ventes/mois"),
            (start+timedelta(days=1), "Carrousel", "5 idées déco mariage petit budget", "Insta", "Produits: arche blanc/or, chemin gaze"),
            (start+timedelta(days=2), "Stories", "Sondage Team Boy/Girl + coulisses", "Insta", "Engagement"),
            (start+timedelta(days=3), "Reel", "Avant/après table mariage", "TikTok/Insta", "Transformation"),
            (start+timedelta(days=4), "Carrousel", "Thème anniversaire licorne best-seller 2024", "Insta", "Kit 70pcs"),
            (start+timedelta(days=5), "UGC", "Repartage client", "Insta/TikTok", "Avec autorisation"),
            (start+timedelta(days=6), "Inspiration", "Moodboard rose/bleu pastel", "Pinterest", "SEO visuel"),
        ]
        return [{"date": d.strftime("%Y-%m-%d"), "type": t, "title": title, "channel": ch, "note": n} for d,t,title,ch,n in plan]
