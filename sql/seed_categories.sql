-- SEED CATEGORIES - L'Effet Waouh V2
-- 4 univers principaux + sous-catégories

INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position, meta_title) VALUES
-- UNIVERS RACINES
('mariage', 'Mariage', NULL, 'Tout pour un mariage waouh : cierges, confettis, livres d''or, déco', 'mariage', 1, 'Décoration et gadgets mariage - L''Effet Waouh'),
('naissance', 'Naissance', NULL, 'Annoncer et célébrer l''arrivée de bébé', 'naissance', 2, 'Décoration naissance bébé'),
('gender-reveal', 'Gender Reveal', NULL, 'Annonce du sexe de bébé : ballons, fumigènes, confettis rose/bleu', 'gender_reveal', 3, 'Gender Reveal rose ou bleu - Annonce sexe bébé'),
('baby-shower', 'Baby Shower', NULL, 'Décoration et jeux pour baby shower', 'baby_shower', 4, 'Baby Shower décoration'),
('evjf-evjg', 'EVJF / EVJG', NULL, 'Accessoires pour enterrements de vie de jeune fille/garçon', 'evjf', 5, 'EVJF EVJG accessoires'),
('bapteme', 'Baptême', NULL, 'Décoration baptême fille et garçon', 'bapteme', 6, 'Décoration baptême');

-- SOUS-CATEGORIES MARIAGE
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('mariage-sortie-mairie', 'Sortie de Mairie', (SELECT id FROM categories WHERE slug='mariage'), 'Bulles, confettis, pétales', 'mariage', 1),
('mariage-cierges', 'Cierges Magiques', (SELECT id FROM categories WHERE slug='mariage'), 'Cierges magiques lots 20 à 200', 'mariage', 2),
('mariage-livre-or', 'Livres d''Or', (SELECT id FROM categories WHERE slug='mariage'), 'Livres d''or audio, papier, urnes', 'mariage', 3),
('mariage-deco-lumineuse', 'Déco Lumineuse', (SELECT id FROM categories WHERE slug='mariage'), 'Néons, lettres LOVE, guirlandes', 'mariage', 4),
('mariage-photobooth', 'Photobooth & Accessoires', (SELECT id FROM categories WHERE slug='mariage'), 'Cadres, accessoires, impressions', 'mariage', 5),
('mariage-confettis', 'Confettis & Pétales', (SELECT id FROM categories WHERE slug='mariage'), 'Confettis biodégradables, pétales', 'mariage', 6);

-- SOUS-CATEGORIES GENDER REVEAL (CRITIQUE POUR TON BUSINESS)
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('gender-ballon', 'Ballons Gender Reveal', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Ballons éclatables 90cm avec confettis rose/bleu', 'gender_reveal', 1),
('gender-fumigene', 'Fumigènes Couleur', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Fumigènes rose et bleu, lot de 2 à 6', 'gender_reveal', 2),
('gender-canon-confetti', 'Canons à Confettis', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Canons confettis rose/bleu main et CO2', 'gender_reveal', 3),
('gender-boite-surprise', 'Boîtes Surprises', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Boîtes à ouvrir avec ballons intérieurs', 'gender_reveal', 4),
('gender-carte-gratter', 'Cartes à Gratter', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Cartes Boy or Girl à gratter lot 10', 'gender_reveal', 5),
('gender-deco', 'Déco Complète', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Kits arche ballons, guirlandes Boy or Girl', 'gender_reveal', 6),
('gender-poudre-holi', 'Poudre Holi & Bombe', (SELECT id FROM categories WHERE slug='gender-reveal'), 'Poudre rose/bleu pour photos', 'gender_reveal', 7);

-- SOUS-CATEGORIES NAISSANCE
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('naissance-annonce', 'Annonce Naissance', (SELECT id FROM categories WHERE slug='naissance'), 'Ballons, cartes, banderoles Bienvenue Bébé', 'naissance', 1),
('naissance-deco-chambre', 'Déco Chambre', (SELECT id FROM categories WHERE slug='naissance'), 'Guirlandes, mobiles, lettres', 'naissance', 2),
('naissance-souvenir', 'Souvenirs & Empreintes', (SELECT id FROM categories WHERE slug='naissance'), 'Kits empreintes, boîtes souvenirs', 'naissance', 3),
('naissance-livre-or', 'Livre d''Or Naissance', (SELECT id FROM categories WHERE slug='naissance'), 'Livres d''or et urnes', 'naissance', 4);

-- SOUS-CATEGORIES BABY SHOWER
INSERT OR IGNORE INTO categories(slug, name, parent_id, description, event_type, position) VALUES
('baby-shower-deco', 'Déco Baby Shower', (SELECT id FROM categories WHERE slug='baby-shower'), 'Kits complets fille/garçon/mixte', 'baby_shower', 1),
('baby-shower-jeux', 'Jeux & Animations', (SELECT id FROM categories WHERE slug='baby-shower'), 'Cartes pronostics, jeux', 'baby_shower', 2);
