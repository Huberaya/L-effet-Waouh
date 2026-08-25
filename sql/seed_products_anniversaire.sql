-- SEED ANNIVERSAIRE - 40 produits (enfant, adulte, 18,30,40,50,60, thèmes)
-- Basé recherche web: licorne, super-héros, sirène, dino, safari, cosmos, Harry Potter, Barbie, Glow Party best-sellers 2024

-- Kits anniversaire enfant
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('ANN-LICORNE-200', 'kit-anniversaire-licorne-70pcs', 'Kit Anniversaire Licorne 70pcs', 'Kit complet licorne pastel', 20.75, 24.90, 8, 40, 'anniversaire', 1),
('ANN-PRINCESSE-201', 'kit-anniversaire-princesse-60pcs', 'Kit Princesse 60pcs - Château Couronne', 'Kit princesse rose gold', 20.75, 24.90, 8, 35, 'anniversaire', 1),
('ANN-SUPER-202', 'kit-anniversaire-super-heros-60pcs', 'Kit Super-Héros 60pcs', 'Spiderman Batman Avengers', 20.75, 24.90, 8, 30, 'anniversaire', 1),
('ANN-FOOT-203', 'kit-anniversaire-football-50pcs', 'Kit Football 50pcs', 'Ballon foot + vert', 16.58, 19.90, 6, 30, 'anniversaire', 0),
('ANN-ESPACE-204', 'kit-anniversaire-espace-60pcs', 'Kit Espace 60pcs - Fusée Planètes', 'Thème espace astronaute', 20.75, 24.90, 8, 25, 'anniversaire', 0),
('ANN-DINO-205', 'kit-anniversaire-dinosaure-50pcs', 'Kit Dinosaure 50pcs', 'Dino jurassique', 16.58, 19.90, 6, 30, 'anniversaire', 0),
('ANN-SIRENE-206', 'kit-anniversaire-sirene-60pcs', 'Kit Sirène 60pcs', 'Sirène aquatique coquillages', 20.75, 24.90, 8, 25, 'anniversaire', 0),
('ANN-SAFARI-207', 'kit-anniversaire-safari-50pcs', 'Kit Safari 50pcs - Jungle Animaux', 'Safari savane animaux', 16.58, 19.90, 6, 20, 'anniversaire', 0),
('ANN-HP-208', 'kit-anniversaire-harry-potter-60pcs', 'Kit Harry Potter 60pcs - Poudlard', 'Bougies flottantes, potions', 24.08, 28.90, 10, 20, 'anniversaire', 1),
('ANN-BARBIE-209', 'kit-anniversaire-barbie-50pcs', 'Kit Barbie 50pcs Rose Glamour', 'Rose paillettes néon', 20.75, 24.90, 8, 25, 'anniversaire', 0),
('ANN-GLOW-210', 'kit-anniversaire-glow-party-50pcs', 'Kit Glow Party 50pcs Fluo', 'Blacklight fluo néon', 20.75, 24.90, 8, 20, 'anniversaire', 0),
('ANN-ANIMAUX-211', 'kit-anniversaire-animaux-kawaii-50pcs', 'Kit Animaux Kawaii 50pcs', 'Animaux mignons pastel', 16.58, 19.90, 6, 20, 'anniversaire', 0);

-- Anniversaire adulte
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type) VALUES
('ANN-ADULTE-220', 'kit-anniversaire-adulte-rose-gold-50pcs', 'Kit Adulte Rose Gold 50pcs - Chic', 'Rose gold élégant', 20.75, 24.90, 8, 30, 'anniversaire'),
('ANN-ADULTE-221', 'kit-anniversaire-adulte-noir-or-50pcs', 'Kit Adulte Noir & Or 50pcs', 'Noir or chic', 20.75, 24.90, 8, 25, 'anniversaire'),
('ANN-ADULTE-222', 'kit-anniversaire-adulte-tropical-50pcs', 'Kit Tropical 50pcs - Flamant Ananas', 'Tropical adulte', 20.75, 24.90, 8, 20, 'anniversaire');

-- Anniversaires âges (18,20,30,40,50,60)
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('ANN-18-230', 'kit-anniversaire-18-ans-noir-or-40pcs', 'Kit 18 Ans Noir & Or 40pcs', 'Majorité 18 ans', 16.58, 19.90, 6, 30, 'anniversaire', 1),
('ANN-20-231', 'kit-anniversaire-20-ans-40pcs', 'Kit 20 Ans 40pcs', 'Déco 20 ans', 16.58, 19.90, 6, 25, 'anniversaire', 0),
('ANN-30-232', 'kit-anniversaire-30-ans-rose-gold-50pcs', 'Kit 30 Ans Rose Gold 50pcs - Best-seller', 'Best-seller 30 ans', 20.75, 24.90, 8, 40, 'anniversaire', 1),
('ANN-40-233', 'kit-anniversaire-40-ans-noir-or-50pcs', 'Kit 40 Ans Noir Or 50pcs', 'Déco 40 ans chic', 20.75, 24.90, 8, 30, 'anniversaire', 0),
('ANN-50-234', 'kit-anniversaire-50-ans-or-50pcs', 'Kit 50 Ans Or 50pcs', 'Déco 50 ans or', 20.75, 24.90, 8, 25, 'anniversaire', 0),
('ANN-60-235', 'kit-anniversaire-60-ans-50pcs', 'Kit 60 Ans 50pcs', 'Déco 60 ans', 20.75, 24.90, 8, 20, 'anniversaire', 0),
('ANN-1AN-236', 'kit-anniversaire-1-an-40pcs', 'Kit 1 An 40pcs - Première bougie', 'Déco 1 an pastel', 16.58, 19.90, 6, 30, 'anniversaire', 0);

-- Accessoires anniversaire complémentaires
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type) VALUES
('ANN-BOUGIE-240', 'bougies-chiffres-anniversaire-or', 'Bougies Chiffres Or - 0-9', 'Bougie chiffre or 5cm', 2.42, 2.90, 0.7, 100, 'anniversaire'),
('ANN-PINATA-241', 'pinata-anniversaire-licorne', 'Pinata Licorne', 'Pinata à casser + bâton', 16.58, 19.90, 6, 20, 'anniversaire'),
('ANN-CADEAU-242', 'sachets-cadeaux-invites-anniversaire-lot-20', 'Sachets Cadeaux Invités Lot 20', 'Pochons + étiquettes lot 20', 12.42, 14.90, 4.5, 50, 'anniversaire'),
('ANN-VAISSELLE-243', 'vaisselle-anniversaire-jetable-20-pers', 'Vaisselle Jetable 20 Pers - Thème au choix', 'Assiettes gobelets serviettes 20 pers', 16.58, 19.90, 6, 40, 'anniversaire'),
('ANN-GUIRLANDE-244', 'guirlande-happy-birthday-or', 'Guirlande Happy Birthday Or', 'Guirlande paillettes or 2m', 6.58, 7.90, 2, 60, 'anniversaire'),
('ANN-BALLON-CHIFFRE-245', 'ballons-chiffres-80cm-or', 'Ballons Chiffres 80cm Or', 'Ballons foil chiffres 80cm', 8.25, 9.90, 2.8, 50, 'anniversaire');
