-- SEED KITS + PERSONNALISABLES - Stratégie panier moyen x4 + personnalisation axe stratégique

-- KITS ÉVÉNEMENTIELS (packs prêts à l'emploi)
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
-- Kit Mariage
('KIT-MAR-400', 'kit-mariage-essentiel-50-pers', 'Kit Mariage Essentiel 50 Personnes', 'Tout pour sortie mairie 50 pers', 'Kit complet 50 pers: 50 cierges magiques 40cm + 1kg confettis bio blancs + 24 tubes bulles + 20 marque-places bois cœur + 1 livre or bois. Économie 15% vs achat séparé. Parfait pour mariage 50 invités.', 74.08, 88.90, 32, 20, 'mariage', 1),
('KIT-MAR-401', 'kit-mariage-table-20-pers', 'Kit Table Mariage 20 Personnes - Chic', 'Déco table 20 pers complète', 'Kit table 20 pers: 1 chemin gaze 6m + 20 marque-places + 1 guirlande eucalyptus + 20 pochons lavande + 5 bougies. Élégant.', 62.42, 74.90, 26, 15, 'mariage', 1),
('KIT-MAR-402', 'kit-evjf-complete-10-pers', 'Kit EVJF Complet 10 Personnes', 'Tout pour EVJF 10 pers', 'Kit EVJF: 10 bandeaux Team Bride + voile + 30 accessoires (lunettes, tatouages) + 10 sachets cadeaux + 1 pinata. Fête garantie.', 54.08, 64.90, 22, 20, 'mariage', 1),

-- Kit Gender Reveal
('KIT-GR-410', 'kit-gender-reveal-premium-30-pers', 'Kit Gender Reveal Premium 30 Pers', 'Fête complète 30 pers', 'Kit premium 30 pers: 1 ballon 90cm + 4 fumigènes + 10 canons + 1 arche 85pcs + 30 badges Team Boy/Girl + 20 cartes pronostics + 30 cartes à gratter + déco table. Tout compris.', 107.42, 128.90, 48, 15, 'gender_reveal', 1),
('KIT-GR-411', 'kit-gender-reveal-intime-10-pers', 'Kit Gender Reveal Intime 10 Pers', 'Pour famille proche 10 pers', 'Kit intime 10 pers: 1 ballon 90cm + 2 fumigènes + 3 canons + 10 badges + 10 cartes à gratter. Parfait pour annonce famille.', 41.58, 49.90, 18, 30, 'gender_reveal', 1),

-- Kit Baby Shower
('KIT-BS-420', 'kit-baby-shower-fille-20-pers-complet', 'Kit Baby Shower Fille Complet 20 Pers', 'Tout pour Baby Shower fille 20 pers', 'Kit complet 20 pers fille: 1 kit déco 70pcs rose gold + 20 vaisselle (assiettes gobelets) + 20 jeux pronostics + 20 cadeaux invités bougies + 1 guirlande personnalisée prénom. Tout pour organiser.', 74.08, 88.90, 32, 20, 'baby_shower', 1),
('KIT-BS-421', 'kit-baby-shower-garcon-20-pers-complet', 'Kit Baby Shower Garçon Complet 20 Pers', 'Tout pour Baby Shower garçon 20 pers', 'Kit complet 20 pers garçon: 1 kit déco 70pcs bleu gold + 20 vaisselle + 20 jeux + 20 cadeaux + guirlande prénom. Tout compris.', 74.08, 88.90, 32, 20, 'baby_shower', 1),

-- Kit Naissance
('KIT-NAIS-430', 'kit-naissance-bienvenue-bebe-complet', 'Kit Naissance Bienvenue Bébé Complet', 'Tout pour annoncer bébé', 'Kit complet: 1 guirlande Bienvenue Bébé + 1 ballons BABY + 1 kit empreintes + 1 boîte souvenirs + 1 affiche personnalisée + 1 livre or. Parfait pour annoncer.', 62.42, 74.90, 26, 20, 'naissance', 1),
('KIT-NAIS-431', 'kit-annonce-naissance-parents', 'Kit Annonce Naissance Parents', 'Pour grands-parents famille', 'Kit annonce: 10 cartes à gratter annonce + 5 ballons bulle personnalisés + 1 guirlande. Pour annoncer aux proches.', 37.42, 44.90, 15, 25, 'naissance', 0),

-- Kit Baptême
('KIT-BAP-440', 'kit-bapteme-20-invites-complet', 'Kit Baptême 20 Invités Complet', 'Tout pour baptême 20 invités', 'Kit complet 20 invités: 20 bougies personnalisées + 20 contenants dragées plexi + 20 magnets + déco table (chemin + centre) + 1 guirlande prénom bois. Tout pour baptême.', 107.42, 128.90, 48, 15, 'bapteme', 1),
('KIT-BAP-441', 'kit-bapteme-parrain-marraine-luxe', 'Kit Baptême Parrain Marraine Luxe', 'Coffret luxe parrain marraine', 'Coffret luxe: 2 bougies + 2 cadres + 2 médailles + 1 boîte souvenirs + 1 timbale. Pour parrain marraine.', 74.08, 88.90, 32, 10, 'bapteme', 0),

-- Kit Anniversaire
('KIT-ANN-450', 'kit-anniversaire-licorne-15-enfants', 'Kit Anniversaire Licorne 15 Enfants', 'Tout pour anniv licorne 15 enfants', 'Kit complet 15 enfants licorne: 1 kit déco 70pcs + 15 vaisselle + 1 pinata licorne + 15 sachets cadeaux + 1 guirlande Happy Birthday + 15 chapeaux. Fête garantie.', 62.42, 74.90, 26, 20, 'anniversaire', 1),
('KIT-ANN-451', 'kit-anniversaire-30-ans-20-pers', 'Kit Anniversaire 30 Ans 20 Pers - Rose Gold', 'Tout pour 30 ans 20 pers', 'Kit complet 20 pers 30 ans: 1 kit déco 50pcs rose gold + 20 vaisselle + 20 lunettes + 1 ballons chiffres 30 + 1 guirlande + 20 sachets. Best-seller adulte.', 62.42, 74.90, 26, 25, 'anniversaire', 1),
('KIT-ANN-452', 'kit-anniversaire-harry-potter-12-enfants', 'Kit Harry Potter 12 Enfants - Poudlard', 'Tout pour anniv Harry Potter', 'Kit complet 12 enfants: 1 kit déco 60pcs + 12 vaisselle + 12 baguettes magiques + 1 pinata + jeux. Magie garantie.', 70.75, 84.90, 32, 15, 'anniversaire', 1);

-- PRODUITS PERSONNALISABLES (axe stratégique)
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('PERSO-AFFICHE-500', 'affiche-personnalisee-prenom-date-poids', 'Affiche Personnalisée Prénom Date Poids A4', 'Affiche naissance/baptême personnalisée', 'Affiche A4 personnalisée avec prénom, date, poids, taille, heure. Design épuré minimal, typo serif. Impression haute qualité. Parfait pour naissance, baptême, anniversaire 1 an. Aperçu avant commande.', 10.75, 12.90, 3.5, 100, 'multi', 1),
('PERSO-BALLON-501', 'ballon-bulle-personnalise-prenom-confettis', 'Ballon Bulle Personnalisé Prénom + Confettis 60cm', 'Ballon transparent 60cm personnalisé', 'Ballon bulle transparent 60cm + confettis + prénom vinyle + ruban. Personnalisable prénom, couleur confettis. Sans hélium. Best-seller personnalisé.', 15.75, 18.90, 5, 50, 'multi', 1),
('PERSO-BOUGIE-502', 'bougie-personnalisee-prenom-date-70g', 'Bougie Personnalisée Prénom Date 70g', 'Bougie soja personnalisée 70g', 'Bougie soja 70g verre ambré + étiquette personnalisée prénom date message. Main atelier. Pour mariage, baptême, naissance, anniversaire. Parfait pour cadeaux invités.', 5.75, 6.90, 2, 100, 'multi', 1),
('PERSO-LIVRE-OR-503', 'livre-or-bois-personnalise-prenom-date', 'Livre d''Or Bois Personnalisé Prénom Date', 'Livre or bois gravé personnalisé', 'Livre d''or bois 30x30cm gravé prénom date + message. 50 pages kraft. Pour mariage, naissance, baptême, anniversaire. Aperçu gravure avant commande.', 29.08, 34.90, 11, 20, 'multi', 1),
('PERSO-ETIQUETTE-504', 'etiquettes-personnalisees-rondes-4cm-lot-30', 'Étiquettes Personnalisées Rondes 4cm Lot 30', 'Étiquettes autocollantes personnalisées lot 30', 'Étiquettes autocollantes rondes 4cm personnalisées prénom date motif. Pour contenants dragées, bougies, pochons. Lot 30.', 8.25, 9.90, 2.5, 80, 'multi', 0),
('PERSO-BANDEROLE-505', 'banderole-personnalisee-prenom-tissu-2m', 'Banderole Personnalisée Prénom Tissu 2m', 'Banderole tissu personnalisée 2m', 'Banderole tissu 2m personnalisée prénom + message. Pour Baby Shower, baptême, anniversaire, mariage. Réutilisable.', 16.58, 19.90, 6, 30, 'multi', 0),
('PERSO-MAGNET-506', 'magnet-photo-personnalise-5cm-lot-15', 'Magnet Photo Personnalisé 5cm Lot 15', 'Magnets photo prénom lot 15', 'Magnets 5cm avec photo + prénom date. Pour baptême, naissance, mariage, anniversaire. Les invités gardent sur frigo.', 16.58, 19.90, 6, 40, 'multi', 0),
('PERSO-MUG-507', 'mug-personnalise-prenom-photo', 'Mug Personnalisé Prénom Photo', 'Mug céramique personnalisé', 'Mug céramique 33cl personnalisé prénom + photo + date. Pour cadeaux parents, parrain marraine, témoins, fête des mères/pères.', 10.75, 12.90, 4, 40, 'multi', 0),
('PERSO-CADRE-508', 'cadre-personnalise-bois-prenom-date', 'Cadre Personnalisé Bois Prénom Date', 'Cadre bois 20x20cm personnalisé', 'Cadre bois clair 20x20cm personnalisé prénom date. Pour naissance, baptême, mariage. Souvenir.', 14.08, 16.90, 5, 25, 'multi', 0);
