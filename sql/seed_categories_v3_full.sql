-- SEED CATEGORIES V3 FULL - 80+ catégories pour marque grands moments de vie
-- Date: 2026-08-25 - Mission refonte complète

-- Nettoie anciennes catégories si besoin (garde id)
-- On utilise INSERT OR IGNORE pour ne pas dupliquer

-- ===== RACINES PRINCIPALES (10) =====
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position, meta_title) VALUES
('mariage', 'Mariage', NULL, 'Tout pour un mariage inoubliable: décoration, gadgets, cadeaux invités, jeux, photobooth, EVJF/EVG, personnalisés', 'mariage', 1, 'Décoration mariage, cadeaux invités, accessoires - L''Effet Waouh'),
('gender-reveal', 'Gender Reveal', NULL, 'Annonce sexe bébé: ballons 90cm, confettis, fumigènes, boîtes surprise, kits complets rose/bleu', 'gender_reveal', 2, 'Gender Reveal rose bleu - Ballon éclatable, fumigène, canon confettis'),
('baby-shower', 'Baby Shower', NULL, 'Tout pour organiser Baby Shower: kits déco 70pcs, ballons, vaisselle, jeux, cadeaux invités', 'baby_shower', 3, 'Baby Shower décoration kit - Fille garçon - L''Effet Waouh'),
('naissance', 'Naissance', NULL, 'Célébrer bébé: cadeaux naissance, décoration, boîtes souvenirs, cartes étapes, affiches personnalisées', 'naissance', 4, 'Cadeau naissance, décoration bébé - Boîte souvenirs, kit empreintes'),
('bapteme', 'Baptême', NULL, 'Baptême fille garçon: décoration, bougies personnalisées, contenants dragées, cadeaux parrain marraine', 'bapteme', 5, 'Baptême décoration cadeaux invités - Bougie personnalisée, dragées'),
('anniversaire', 'Anniversaire', NULL, 'Anniversaire enfant adulte: déco, kits, thèmes licorne, princesse, super-héros, football, espace', 'anniversaire', 6, 'Décoration anniversaire enfant adulte - Thème licorne, princesse, 18 30 40 ans'),
('personnalise', 'Personnalisé', NULL, 'Produits personnalisables: prénom, date, message, photo, couleur - Aperçu avant commande', 'multi', 7, 'Produits personnalisés mariage naissance baptême - Prénom date photo'),
('kits', 'Kits Événementiels', NULL, 'Packs prêts à l''emploi: Kit Mariage, Gender Reveal, Baby Shower, Naissance, Baptême, Anniversaire - Panier moyen x4', 'multi', 8, 'Kits événementiels - Tout pour organiser fête - Mariage Gender Reveal Baby Shower'),
('cadeaux', 'Cadeaux', NULL, 'Cadeaux invités, témoins, parents, parrain marraine, maîtresse - Personnalisables', 'multi', 9, 'Cadeaux invités mariage baptême - Personnalisés - Témoins parrain marraine'),
('promotions', 'Promotions', NULL, 'Best-sellers, nouveautés, -20%, packs, livraison gratuite', 'multi', 10, 'Promotions décoration fête - Best-sellers - Packs');

-- ===== MARIAGE - 15 sous-catégories =====
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('mariage-decoration', 'Décoration Mariage', (SELECT id FROM categories WHERE slug='mariage'), 'Guirlandes, centres de table, déco salle', 'mariage', 1),
('mariage-decoration-salle', 'Décoration Salle', (SELECT id FROM categories WHERE slug='mariage'), 'Arches, rideaux lumineux, lettres lumineuses LOVE', 'mariage', 2),
('mariage-decoration-table', 'Décoration Table', (SELECT id FROM categories WHERE slug='mariage'), 'Chemins de table, marque-places, centres de table, bougies', 'mariage', 3),
('mariage-decoration-voiture', 'Décoration Voiture', (SELECT id FROM categories WHERE slug='mariage'), 'Rubans, fleurs, Just Married, ballons voiture', 'mariage', 4),
('mariage-gadgets', 'Gadgets & Effets Waouh', (SELECT id FROM categories WHERE slug='mariage'), 'Cierges magiques, confettis, bulles, fumée, canons CO2', 'mariage', 5),
('mariage-accessoires-invites', 'Accessoires Invités', (SELECT id FROM categories WHERE slug='mariage'), 'Chapeaux, lunettes, bracelets, éventails', 'mariage', 6),
('mariage-accessoires-maries', 'Accessoires Mariés', (SELECT id FROM categories WHERE slug='mariage'), 'Voile, couronne, nœud papillon, jarretière', 'mariage', 7),
('mariage-cadeaux-invites', 'Cadeaux Invités', (SELECT id FROM categories WHERE slug='mariage'), 'Dragées, bougies, savons, pochons personnalisés', 'mariage', 8),
('mariage-jeux', 'Jeux Mariage', (SELECT id FROM categories WHERE slug='mariage'), 'Jeux EVJF, quizz, animation table, livre or', 'mariage', 9),
('mariage-photobooth', 'Photobooth', (SELECT id FROM categories WHERE slug='mariage'), 'Cadres, accessoires, impressions, 360', 'mariage', 10),
('mariage-evjf-evg', 'EVJF / EVG', (SELECT id FROM categories WHERE slug='mariage'), 'Accessoires enterrement vie jeune fille/garçon, déguisements', 'mariage', 11),
('mariage-personnalises', 'Personnalisés Mariage', (SELECT id FROM categories WHERE slug='mariage'), 'Néons prénom, livre or bois gravé, urne personnalisée', 'mariage', 12),
('mariage-kits', 'Kits Mariage', (SELECT id FROM categories WHERE slug='mariage'), 'Kits sortie mairie 50 pers, déco table 20 pers', 'mariage', 13),
('mariage-ceremonie', 'Cérémonie', (SELECT id FROM categories WHERE slug='mariage'), 'Arche cérémonie, pétales, coussin alliances', 'mariage', 14),
('mariage-temoins', 'Témoins & Famille', (SELECT id FROM categories WHERE slug='mariage'), 'Cadeaux témoins, parrain, marraine, parents', 'mariage', 15);

-- ===== GENDER REVEAL - 13 sous-catégories =====
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('gender-reveal-ballons', 'Ballons Gender Reveal', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Ballons éclatables 90cm noir + confettis rose/bleu', 'gender_reveal', 1),
('gender-reveal-confettis', 'Confettis Rose/Bleu', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Confettis biodégradables, canons 30cm', 'gender_reveal', 2),
('gender-reveal-fumigenes', 'Fumigènes Couleur', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Fumigènes 60s rose/bleu, lot 2, T1 vente libre', 'gender_reveal', 3),
('gender-reveal-boites', 'Boîtes Surprise', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Boîtes 60cm avec ballons hélium intérieur', 'gender_reveal', 4),
('gender-reveal-kits-revelation', 'Kits Révélation', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Kits avec plusieurs méthodes révélation', 'gender_reveal', 5),
('gender-reveal-deco', 'Déco Rose/Bleu', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Arches ballons 85pcs, guirlandes Boy or Girl', 'gender_reveal', 6),
('gender-reveal-photo', 'Accessoires Photo', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Cadres, pancartes, photobooth', 'gender_reveal', 7),
('gender-reveal-jeux', 'Jeux Gender Reveal', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Cartes pronostics, jeux devinettes', 'gender_reveal', 8),
('gender-reveal-cartes', 'Cartes à Gratter', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Cartes Boy or Girl à gratter lot 10', 'gender_reveal', 9),
('gender-reveal-badges', 'Badges & Accessoires Invités', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Badges Team Boy/Girl, bracelets', 'gender_reveal', 10),
('gender-reveal-table', 'Décoration Table', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Vaisselle rose/bleu, centres de table', 'gender_reveal', 11),
('gender-reveal-kits-complets', 'Kits Complets', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Kits fête 20 pers tout compris', 'gender_reveal', 12),
('gender-reveal-personnalises', 'Personnalisables', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Ballon prénom, carte photo', 'gender_reveal', 13);

-- ===== NAISSANCE - 11 sous-catégories =====
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('naissance-cadeaux', 'Cadeaux Naissance', (SELECT id FROM categories WHERE slug='naissance'), 'Cadeaux bébé, parents, coffrets', 'naissance', 1),
('naissance-decoration', 'Décoration Naissance', (SELECT id FROM categories WHERE slug='naissance'), 'Guirlandes Bienvenue Bébé, ballons BABY', 'naissance', 2),
('naissance-boites', 'Boîtes Souvenirs', (SELECT id FROM categories WHERE slug='naissance'), 'Boîtes bois souvenirs bébé', 'naissance', 3),
('naissance-photo', 'Accessoires Photo', (SELECT id FROM categories WHERE slug='naissance'), 'Cadres, accessoires photo naissance', 'naissance', 4),
('naissance-cartes-etapes', 'Cartes Étapes', (SELECT id FROM categories WHERE slug='naissance'), 'Cartes mois, première fois', 'naissance', 5),
('naissance-affiches', 'Affiches Naissance', (SELECT id FROM categories WHERE slug='naissance'), 'Affiches personnalisées prénom date poids', 'naissance', 6),
('naissance-personnalises', 'Personnalisés Naissance', (SELECT id FROM categories WHERE slug='naissance'), 'Ballon bulle prénom, affiche', 'naissance', 7),
('naissance-bebe', 'Cadeaux Bébé', (SELECT id FROM categories WHERE slug='naissance'), 'Doudou, couverture, vêtements', 'naissance', 8),
('naissance-parents', 'Cadeaux Parents', (SELECT id FROM categories WHERE slug='naissance'), 'Mug, cadre, bijou parents', 'naissance', 9),
('naissance-coffrets', 'Coffrets Naissance', (SELECT id FROM categories WHERE slug='naissance'), 'Coffrets complets cadeaux', 'naissance', 10),
('naissance-annonce', 'Annonce Naissance', (SELECT id FROM categories WHERE slug='naissance'), 'Cartes annonce, ballons annonce', 'naissance', 11);

-- ===== BABY SHOWER - 10 sous-catégories =====
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('baby-shower-kits-deco', 'Kits Décoration', (SELECT id FROM categories WHERE slug='baby-shower'), 'Kits 70pcs fille/garçon/mixte', 'baby_shower', 1),
('baby-shower-ballons', 'Ballons Baby Shower', (SELECT id FROM categories WHERE slug='baby-shower'), 'Ballons Oh Baby, Baby Shower', 'baby_shower', 2),
('baby-shower-guirlandes', 'Guirlandes', (SELECT id FROM categories WHERE slug='baby-shower'), 'Guirlandes Oh Baby, Baby Shower', 'baby_shower', 3),
('baby-shower-vaisselle', 'Vaisselle', (SELECT id FROM categories WHERE slug='baby-shower'), 'Assiettes, gobelets, serviettes thème', 'baby_shower', 4),
('baby-shower-table', 'Décoration Table', (SELECT id FROM categories WHERE slug='baby-shower'), 'Centres de table, confettis table', 'baby_shower', 5),
('baby-shower-jeux', 'Jeux Baby Shower', (SELECT id FROM categories WHERE slug='baby-shower'), 'Cartes pronostics, jeux devinettes bébé', 'baby_shower', 6),
('baby-shower-cadeaux', 'Cadeaux Invités', (SELECT id FROM categories WHERE slug='baby-shower'), 'Bougies, savons, pochons', 'baby_shower', 7),
('baby-shower-photo', 'Accessoires Photo', (SELECT id FROM categories WHERE slug='baby-shower'), 'Photobooth, cadres, pancartes', 'baby_shower', 8),
('baby-shower-perso', 'Décoration Personnalisée', (SELECT id FROM categories WHERE slug='baby-shower'), 'Banderole prénom, affiche', 'baby_shower', 9),
('baby-shower-kits-complets', 'Kits Complets', (SELECT id FROM categories WHERE slug='baby-shower'), 'Tout pour organiser Baby Shower 20 pers', 'baby_shower', 10);

-- ===== BAPTÊME - 9 sous-catégories =====
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('bapteme-decoration', 'Décoration Baptême', (SELECT id FROM categories WHERE slug='bapteme'), 'Guirlandes, ballons, arche baptême', 'bapteme', 1),
('bapteme-cadeaux-invites', 'Cadeaux Invités Baptême', (SELECT id FROM categories WHERE slug='bapteme'), 'Bougies personnalisées, dragées, magnets', 'bapteme', 2),
('bapteme-contenants', 'Contenants Dragées', (SELECT id FROM categories WHERE slug='bapteme'), 'Boîtes, pochons, bonbonnières verre', 'bapteme', 3),
('bapteme-bougies', 'Bougies Décoratives', (SELECT id FROM categories WHERE slug='bapteme'), 'Bougies personnalisées prénom date', 'bapteme', 4),
('bapteme-table', 'Décoration Table Baptême', (SELECT id FROM categories WHERE slug='bapteme'), 'Chemins, centres, marque-places', 'bapteme', 5),
('bapteme-souvenirs', 'Souvenirs Baptême', (SELECT id FROM categories WHERE slug='bapteme'), 'Cadres, affiches, boîtes souvenirs', 'bapteme', 6),
('bapteme-coffrets', 'Coffrets Baptême', (SELECT id FROM categories WHERE slug='bapteme'), 'Coffrets cadeaux parrain marraine', 'bapteme', 7),
('bapteme-personnalises', 'Personnalisés Baptême', (SELECT id FROM categories WHERE slug='bapteme'), 'Étiquettes prénom date, magnets photo', 'bapteme', 8),
('bapteme-parrain', 'Parrain Marraine', (SELECT id FROM categories WHERE slug='bapteme'), 'Cadeaux parrain, marraine, parents', 'bapteme', 9);

-- ===== ANNIVERSAIRE - 20+ sous-catégories =====
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('anniversaire-enfant', 'Anniversaire Enfant', (SELECT id FROM categories WHERE slug='anniversaire'), 'Déco anniversaire enfant 1-12 ans', 'anniversaire', 1),
('anniversaire-adulte', 'Anniversaire Adulte', (SELECT id FROM categories WHERE slug='anniversaire'), 'Déco adulte élégante, chic', 'anniversaire', 2),
('anniversaire-1an', '1 An', (SELECT id FROM categories WHERE slug='anniversaire'), 'Première bougie, déco 1 an', 'anniversaire', 3),
('anniversaire-18ans', '18 Ans', (SELECT id FROM categories WHERE slug='anniversaire'), 'Majorité, déco 18 ans', 'anniversaire', 4),
('anniversaire-20ans', '20 Ans', (SELECT id FROM categories WHERE slug='anniversaire'), 'Déco 20 ans', 'anniversaire', 5),
('anniversaire-30ans', '30 Ans', (SELECT id FROM categories WHERE slug='anniversaire'), 'Déco 30 ans, best-seller adulte', 'anniversaire', 6),
('anniversaire-40ans', '40 Ans', (SELECT id FROM categories WHERE slug='anniversaire'), 'Déco 40 ans', 'anniversaire', 7),
('anniversaire-50ans', '50 Ans', (SELECT id FROM categories WHERE slug='anniversaire'), 'Déco 50 ans', 'anniversaire', 8),
('anniversaire-60ans', '60 Ans', (SELECT id FROM categories WHERE slug='anniversaire'), 'Déco 60 ans', 'anniversaire', 9),
('anniversaire-themes', 'Thèmes Anniversaire', (SELECT id FROM categories WHERE slug='anniversaire'), 'Tous les thèmes enfants et adultes', 'anniversaire', 10);

-- Thèmes enfants - potentiel commercial réel (basé recherche web)
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('theme-princesse', 'Princesse', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Thème princesse, château, couronne', 'anniversaire', 1),
('theme-licorne', 'Licorne', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Thème licorne pastel, best-seller 2024', 'anniversaire', 2),
('theme-super-heros', 'Super-Héros', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Spiderman, Batman, Avengers', 'anniversaire', 3),
('theme-football', 'Football', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Thème foot, PSG, ballon', 'anniversaire', 4),
('theme-espace', 'Espace', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Fusée, planètes, astronaute', 'anniversaire', 5),
('theme-animaux', 'Animaux', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Jungle, safari, animaux kawaii', 'anniversaire', 6),
('theme-tropical', 'Tropical', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Flamant, ananas, jungle', 'anniversaire', 7),
('theme-elegant', 'Élégant', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Rose gold, chic, adulte', 'anniversaire', 8),
('theme-annees-80', 'Années 80', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Retro 80s, fluo', 'anniversaire', 9),
('theme-annees-90', 'Années 90', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Retro 90s', 'anniversaire', 10),
('theme-sirene', 'Sirène', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Thème sirène aquatique', 'anniversaire', 11),
('theme-dino', 'Dinosaure', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Dino, jurassique', 'anniversaire', 12),
('theme-safari', 'Safari', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Safari, savane', 'anniversaire', 13),
('theme-harry-potter', 'Harry Potter', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Poudlard, magie', 'anniversaire', 14),
('theme-barbie', 'Barbie', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Rose glamour', 'anniversaire', 15),
('theme-glow', 'Glow Party', (SELECT id FROM categories WHERE slug='anniversaire-themes'), 'Fluo, blacklight', 'anniversaire', 16);

-- ===== AUTRES ÉVÉNEMENTS - Analyse potentiel commercial =====
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('fiancailles', 'Fiançailles', NULL, 'Demande en mariage, décoration fiançailles', 'fiancailles', 20),
('pacs', 'PACS', NULL, 'Célébration PACS', 'pacs', 21),
('retraite', 'Départ Retraite', NULL, 'Fête départ retraite', 'retraite', 22),
('cremaillere', 'Crémaillère', NULL, 'Pendaison crémaillère', 'cremaillere', 23),
('diplome', 'Remise Diplôme', NULL, 'Fête diplôme, graduation', 'diplome', 24),
('saint-valentin', 'Saint-Valentin', NULL, 'Déco Saint-Valentin, cadeaux amoureux', 'saint-valentin', 25),
('fete-meres', 'Fête des Mères', NULL, 'Cadeaux fête des mères personnalisés', 'fete-meres', 26),
('fete-peres', 'Fête des Pères', NULL, 'Cadeaux fête des pères', 'fete-peres', 27),
('noel', 'Noël', NULL, 'Déco Noël, cadeaux, table', 'noel', 28),
('nouvel-an', 'Nouvel An', NULL, 'Déco Nouvel An, cotillons', 'nouvel-an', 29),
('soiree-theme', 'Soirées à Thème', NULL, 'Soirée déguisée, thème', 'soiree-theme', 30),
('entreprise', 'Événements Entreprise', NULL, 'Team building, gala, séminaire', 'entreprise', 31);
