-- NAISSANCE FULL + BABY SHOWER FULL + AUTRES EVENEMENTS

-- NAISSANCE complement (15 produits)
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('NAIS-AFFICHE-100', 'affiche-naissance-personnalisee-prenom-date', 'Affiche Naissance Personnalisee Prenom Date Poids', 'Affiche A4 personnalisee', 10.75, 12.90, 3.5, 50, 'naissance', 1),
('NAIS-CARTE-ETAPE-101', 'cartes-etapes-bebe-30-cartes', 'Cartes Etapes Bebe 30 Cartes', '30 cartes premier mois', 12.42, 14.90, 4, 40, 'naissance', 1),
('NAIS-CADRE-EMPR-102', 'cadre-empreintes-bebe-bois-double', 'Cadre Empreintes Bebe Bois Double', 'Double cadre main pied', 20.75, 24.90, 8, 20, 'naissance', 0),
('NAIS-PELUCHE-103', 'peluche-bebe-personnalisee-prenom', 'Peluche Bebe Personnalisee Prenom', 'Peluche brodee prenom', 16.58, 19.90, 6, 30, 'naissance', 0),
('NAIS-MUSIQUE-104', 'boite-musique-bebe-personnalisee', 'Boite a Musique Bebe Personnalisee', 'Boite musique prenom', 20.75, 24.90, 8, 15, 'naissance', 0),
('NAIS-BAVOIR-105', 'bavoirs-personnalises-bebe-lot-3', 'Bavoirs Personnalises Bebe Lot 3', 'Lot 3 bavoirs prenom', 14.08, 16.90, 5, 30, 'naissance', 0),
('NAIS-COFFRET-106', 'coffret-naissance-bebe-luxe', 'Coffret Naissance Bebe Luxe', 'Coffret complet naissance', 37.42, 44.90, 16, 15, 'naissance', 1),
('NAIS-BALLON-ANNONCE-107', 'ballons-annonce-grossesse-parents', 'Ballons Annonce Grossesse Parents', 'Ballons annonce famille', 12.42, 14.90, 4, 30, 'naissance', 0),
('NAIS-GUIRLANDE-PRENOM-108', 'guirlande-prenom-bebe-bois', 'Guirlande Prenom Bebe Bois', 'Lettres bois prenom 1.5m', 16.58, 19.90, 6, 20, 'naissance', 0),
('NAIS-TAPIS-109', 'tapis-photo-bebe-mois', 'Tapis Photo Bebe Mois', 'Tapis mois + accessoires', 24.08, 28.90, 9, 15, 'naissance', 0),
('NAIS-LIVRE-SOUV-110', 'livre-souvenirs-bebe-premiere-annee', 'Livre Souvenirs Bebe Premiere Annee', 'Livre 80 pages premiere annee', 16.58, 19.90, 6, 25, 'naissance', 0),
('NAIS-BOITE-DENTS-111', 'boite-dents-lait-bebe-bois', 'Boite Dents de Lait Bebe Bois', 'Boite bois dents lait', 12.42, 14.90, 4, 20, 'naissance', 0),
('NAIS-CADEAU-PARENTS-112', 'cadeau-parents-bebe-bougie-mug', 'Cadeau Parents Bebe - Bougie + Mug', 'Coffret parents bougie mug', 20.75, 24.90, 8, 20, 'naissance', 0),
('NAIS-BALLON-BABYSHOWER-113', 'ballon-baby-douche-bebe-fille-garcon', 'Ballon Baby Douche Fille Garcon 90cm', 'Ballon 90cm Boy Girl', 8.25, 9.90, 2.8, 40, 'naissance', 0),
('NAIS-BODY-114', 'body-bebe-personnalise-prenom', 'Body Bebe Personnalise Prenom', 'Body coton personnalise', 10.75, 12.90, 3.8, 40, 'naissance', 0);

-- BABY SHOWER FULL (15 produits)
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('BS-BALLON-120', 'ballons-baby-shower-50pcs-rose-bleu', 'Ballons Baby Shower 50pcs Rose Bleu', 'Lot 50 ballons pastel', 12.42, 14.90, 4, 40, 'baby_shower', 0),
('BS-GUIRLANDE-121', 'guirlande-oh-baby-rose-gold', 'Guirlande Oh Baby Rose Gold', 'Guirlande paillettes 2m', 6.58, 7.90, 2, 50, 'baby_shower', 0),
('BS-VAISSELLE-122', 'vaisselle-baby-shower-20-pers-fille', 'Vaisselle Baby Shower 20 Pers Fille', 'Assiettes gobelets serviettes 20 pers fille', 16.58, 19.90, 6, 30, 'baby_shower', 0),
('BS-VAISSELLE-123', 'vaisselle-baby-shower-20-pers-garcon', 'Vaisselle Baby Shower 20 Pers Garcon', 'Assiettes gobelets serviettes 20 pers garcon', 16.58, 19.90, 6, 30, 'baby_shower', 0),
('BS-JEU-124', 'jeu-baby-shower-pronostics-lot-20', 'Jeu Pronostics Baby Shower Lot 20', 'Cartes pronostics lot 20', 6.58, 7.90, 1.8, 50, 'baby_shower', 0),
('BS-JEU-125', 'jeu-baby-shower-bingo-lot-20', 'Jeu Bingo Baby Shower Lot 20', 'Bingo baby shower lot 20', 6.58, 7.90, 1.8, 40, 'baby_shower', 0),
('BS-CADEAU-126', 'cadeaux-invites-baby-shower-bougies-lot-15', 'Cadeaux Invites Baby Shower Bougies Lot 15', 'Bougies 60g lot 15', 20.75, 24.90, 8, 25, 'baby_shower', 0),
('BS-PHOTOBOOTH-127', 'photobooth-baby-shower-15-accessoires', 'Photobooth Baby Shower 15 Accessoires', 'Accessoires photo 15 pcs', 12.42, 14.90, 4, 30, 'baby_shower', 0),
('BS-BANDEROLE-128', 'banderole-baby-shower-personnalisee-prenom', 'Banderole Baby Shower Personnalisee Prenom', 'Banderole tissu prenom 2m', 16.58, 19.90, 6, 20, 'baby_shower', 0),
('BS-BALLON-BULLE-129', 'ballon-bulle-baby-shower-personnalise', 'Ballon Bulle Baby Shower Personnalise', 'Ballon 60cm personnalise', 15.75, 18.90, 5, 25, 'baby_shower', 0),
('BS-LIVRE-OR-130', 'livre-or-baby-shower-conseils-parents', 'Livre d Or Baby Shower Conseils Parents', '50 cartes conseils', 14.08, 16.90, 5, 20, 'baby_shower', 0),
('BS-DIAPER-131', 'diaper-cake-couche-gateau-baby-shower', 'Diaper Cake Gateau Couches Baby Shower', 'Gateau couches 3 etages', 29.08, 34.90, 12, 10, 'baby_shower', 0),
('BS-SASH-132', 'sash-mom-to-be-baby-shower', 'Sash Mom To Be Baby Shower', 'Echarpe future maman', 8.25, 9.90, 2.8, 30, 'baby_shower', 0),
('BS-COURONNE-133', 'couronne-fleurs-mom-to-be', 'Couronne Fleurs Mom To Be', 'Couronne fleurs future maman', 16.58, 19.90, 6, 20, 'baby_shower', 0),
('BS-CONFETTI-134', 'confettis-baby-shower-bouteille-100g', 'Confettis Baby Shower Bouteille 100g', 'Confettis biberons 100g', 4.08, 4.90, 1.2, 40, 'baby_shower', 0);

-- AUTRES EVENEMENTS (12 produits a potentiel moyen-eleve)
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type) VALUES
('AUTRE-FIANC-150', 'kit-fiancailles-ballon-bague-50pcs', 'Kit Fiancailles Ballon Bague 50pcs', 'Deco fiancailles', 16.58, 19.90, 6, 20, 'autre'),
('AUTRE-PACS-151', 'kit-pacs-deco-40pcs', 'Kit PACS Deco 40pcs', 'Deco PACS', 16.58, 19.90, 6, 15, 'autre'),
('AUTRE-CREMA-152', 'kit-cremaillere-40pcs', 'Kit Cremaillere 40pcs', 'Deco cremaillere', 16.58, 19.90, 6, 15, 'autre'),
('AUTRE-DIP-153', 'kit-diplome-felicitations-30pcs', 'Kit Diplome Felicitations 30pcs', 'Deco diplome', 12.42, 14.90, 4, 20, 'autre'),
('AUTRE-RETRAITE-154', 'kit-retraite-40pcs-bonne-retraite', 'Kit Retraite 40pcs Bonne Retraite', 'Deco retraite', 16.58, 19.90, 6, 15, 'autre'),
('AUTRE-STVAL-155', 'kit-saint-valentin-deco-30pcs', 'Kit Saint Valentin Deco 30pcs', 'Deco St Valentin', 12.42, 14.90, 4, 25, 'autre'),
('AUTRE-NOEL-156', 'kit-noel-deco-50pcs', 'Kit Noel Deco 50pcs', 'Deco Noel', 16.58, 19.90, 6, 30, 'autre'),
('AUTRE-NOUVELAN-157', 'kit-nouvel-an-50pcs-2026', 'Kit Nouvel An 50pcs 2026', 'Deco Nouvel An', 20.75, 24.90, 8, 25, 'autre'),
('AUTRE-FETEMERE-158', 'coffret-fete-meres-bougie-mug', 'Coffret Fete des Meres Bougie + Mug', 'Coffret fete meres', 20.75, 24.90, 8, 20, 'autre'),
('AUTRE-FETEPERE-159', 'coffret-fete-peres-bougie-mug', 'Coffret Fete des Peres Bougie + Mug', 'Coffret fete peres', 20.75, 24.90, 8, 20, 'autre'),
('AUTRE-SOIREE-160', 'kit-soiree-theme-80s-40pcs', 'Kit Soiree Theme Annees 80 40pcs', 'Deco annees 80', 16.58, 19.90, 6, 15, 'autre'),
('AUTRE-ENTR-161', 'kit-entreprise-inauguration-50pcs', 'Kit Entreprise Inauguration 50pcs', 'Deco entreprise', 24.08, 28.90, 10, 10, 'autre');
