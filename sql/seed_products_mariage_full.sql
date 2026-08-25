-- SEED MARIAGE FULL - 30 nouveaux produits pour couvrir tout le mariage
-- Produits d'appel, rentables, complémentaires, premium, best-sellers

-- Décoration salle
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('MAR-ARCHE-100', 'arche-ballons-mariage-blanc-or-200pcs', 'Arche Ballons Mariage Blanc & Or 200pcs', 'Arche complète mariage blanc or', 'Kit arche 200pcs: 120 ballons blancs, 50 or chrome, 20 transparents confettis, 10 coeurs, guirlande, arche métal 3m. Sans hélium. Best-seller déco salle.', 37.42, 44.90, 16, 25, 'mariage', 1),
('MAR-RIDEAU-101', 'rideau-lumineux-led-3x3m-chaud', 'Rideau Lumineux LED 3x3m Blanc Chaud', 'Rideau 300 LED blanc chaud USB', 'Rideau lumineux 3x3m, 300 LED blanc chaud, 8 modes, télécommande, USB. Pour fond cérémonie, photobooth, salle. Réutilisable.', 20.75, 24.90, 8, 30, 'mariage', 1),
('MAR-LETTRES-102', 'lettres-lumineuses-love-40cm', 'Lettres Lumineuses LOVE 40cm', 'LOVE lumineux LED 40cm', 'Lettres LOVE lumineuses LED 40cm hauteur, blanc chaud, piles. Le coin photo iconique. Se loue 250€, se vend 89€. Marge 60%.', 74.08, 88.90, 32, 12, 'mariage', 1),
('MAR-CHEMIN-103', 'chemin-table-gaze-blanc-6m', 'Chemin de Table Gaze Blanc 6m', 'Gaze coton blanc 6m x 30cm', 'Chemin de table gaze de coton blanc 6m x 30cm, lavable, froissé naturel. Pour 10 pers. Best-seller table.', 12.42, 14.90, 4.5, 50, 'mariage', 0),
('MAR-MARQUE-104', 'marque-places-bois-coeur-lot-20', 'Marque-Places Bois Cœur Lot 20', 'Marque-places cœur bois + corde', 'Lot 20 marque-places bois cœur 5cm + corde jute + 20 cartes kraft. Personnalisable prénom.', 10.75, 12.90, 3.8, 60, 'mariage', 0),
('MAR-CENTRE-105', 'centre-table-eucalyptus-artificiel', 'Centre de Table Eucalyptus Artificiel', 'Guirlande eucalyptus 1.8m', 'Guirlande eucalyptus artificiel 1.8m, 6 branches. Pour centre table, arche. Réutilisable, lavable.', 14.08, 16.90, 5.5, 40, 'mariage', 0);

-- Accessoires invités
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type) VALUES
('MAR-LUNETTES-110', 'lunettes-coeur-marie-lot-10', 'Lunettes Cœur Marié Lot 10', 'Lunettes cœur rose gold lot 10', 8.25, 9.90, 2.8, 80, 'mariage'),
('MAR-CHAPEAUX-111', 'chapeaux-fete-mariage-lot-10', 'Chapeaux Fête Mariage Lot 10', 'Chapeaux pointus mariage lot 10', 10.75, 12.90, 4, 50, 'mariage'),
('MAR-EVENTAIL-112', 'eventails-blancs-lot-20', 'Éventails Blancs Lot 20', 'Éventails papier blanc lot 20', 16.58, 19.90, 6, 40, 'mariage'),
('MAR-BRACELET-113', 'bracelets-lumineux-led-lot-30', 'Bracelets Lumineux LED Lot 30', 'Bracelets LED multicolores lot 30', 12.42, 14.90, 4.2, 60, 'mariage');

-- Accessoires mariés
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type) VALUES
('MAR-VOILE-120', 'voile-mariee-court-1m', 'Voile Mariée Court 1m', 'Voile 1m avec peigne', 20.75, 24.90, 7, 20, 'mariage'),
('MAR-COURONNE-121', 'couronne-fleurs-mariee', 'Couronne Fleurs Mariée', 'Couronne fleurs séchées', 24.08, 28.90, 9, 25, 'mariage'),
('MAR-NOEUD-122', 'noeud-papillon-homme-mariage', 'Nœud Papillon Mariage', 'Nœud papillon satin noir/blanc', 10.75, 12.90, 3.5, 30, 'mariage'),
('MAR-JARRETIERE-123', 'jarretiere-mariee-dentelle', 'Jarretière Mariée Dentelle', 'Jarretière dentelle blanche bleue', 12.42, 14.90, 4, 20, 'mariage');

-- Cadeaux invités
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('MAR-DRAGEES-130', 'contenant-dragees-verre-bouchon-liege-lot-20', 'Contenants Dragées Verre Bouchon Liège Lot 20', 'Tubes verre 10ml + bouchon liège lot 20', 'Tubes verre 10ml avec bouchon liège + étiquette personnalisable prénom date. Pour dragées. Best-seller cadeaux invités. 8.2k ventes Etsy.', 14.08, 16.90, 5, 50, 'mariage', 1),
('MAR-BOUGIE-131', 'bougies-personnalisees-mariage-lot-10', 'Bougies Personnalisées Mariage Lot 10', 'Bougies 60g personnalisées lot 10', 'Bougies soja 60g en pot verre ambré + étiquette personnalisée prénom date. Main dans atelier. Best-seller.', 29.08, 34.90, 12, 30, 'mariage', 1),
('MAR-SAVON-132', 'savons-artisanaux-mariage-lot-15', 'Savons Artisanaux Mariage Lot 15', 'Savons 30g personnalisés lot 15', 'Savons artisanaux 30g + étiquette personnalisée. Parfum au choix. Utile et raffiné.', 24.08, 28.90, 9, 35, 'mariage', 0),
('MAR-POCHON-133', 'pochons-lavande-personnalises-lot-20', 'Pochons Lavande Personnalisés Lot 20', 'Pochons lavande + étiquette lot 20', 'Pochons coton avec lavande + étiquette personnalisée. Se conserve longtemps, déco maison invités.', 20.75, 24.90, 8, 40, 'mariage', 0);

-- Jeux
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type) VALUES
('MAR-JEU-140', 'jeu-quizz-maries-cartes-50', 'Jeu Quizz Mariés 50 Cartes', '50 cartes questions mariés', 10.75, 12.90, 3.8, 50, 'mariage'),
('MAR-LIVRE-OR-141', 'livre-or-polaire-mariage-50-fiches', 'Livre d''Or Polaroïd Mariage 50 Fiches', '50 fiches + feutres + corde + pinces', 20.75, 24.90, 8, 30, 'mariage'),
('MAR-URNE-142', 'urne-conseils-maries-bois', 'Urne Conseils Mariés Bois', 'Urne bois + 50 cartes conseils', 24.08, 28.90, 9, 20, 'mariage');

-- Décoration voiture
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type) VALUES
('MAR-VOITURE-150', 'decoration-voiture-mariee-just-married', 'Décoration Voiture Just Married', 'Kit Just Married + rubans + fleurs', 16.58, 19.90, 6, 25, 'mariage'),
('MAR-BALLON-VOIT-151', 'ballons-voiture-mariee-blanc-coeur', 'Ballons Voiture Mariée Blanc Cœur', 'Ballons cœur blanc + rubans lot 10', 10.75, 12.90, 4, 30, 'mariage');

-- EVJF/EVG
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, long_desc, price_ht, price_ttc, cost_price, stock_qty, event_type, is_featured) VALUES
('MAR-EVJF-160', 'kit-evjf-bandeau-voile-future-mariee', 'Kit EVJF Bandeau + Voile Future Mariée', 'Bandeau Team Bride + voile', 'Kit EVJF: 1 bandeau Future Mariée + 6 bandeaux Team Bride + voile + 6 tatouages. Best-seller EVJF.', 20.75, 24.90, 8, 40, 'mariage', 1),
('MAR-EVJF-161', 'accessoires-evjf-lot-30', 'Accessoires EVJF Lot 30', 'Lunettes, chapeaux, tatouages lot 30', 'Lot 30 accessoires EVJF: lunettes cœur, chapeaux, tatouages, ballons. Pour 10 pers.', 24.08, 28.90, 9, 30, 'mariage', 0);

-- Cérémonie & Témoins
INSERT OR IGNORE INTO products(sku, slug, name, short_desc, price_ht, price_ttc, cost_price, stock_qty, event_type) VALUES
('MAR-COUSSIN-170', 'coussin-alliances-lin-blanc', 'Coussin Alliances Lin Blanc', 'Coussin lin 20x20cm', 14.08, 16.90, 5, 20, 'mariage'),
('MAR-CADEAU-TEMOIN-171', 'cadeau-temoin-femme-bougie-bracelet', 'Cadeau Témoin Femme - Bougie + Bracelet', 'Coffret bougie + bracelet + carte', 20.75, 24.90, 8, 25, 'mariage'),
('MAR-CADEAU-TEMOIN-172', 'cadeau-temoin-homme-bouteille', 'Cadeau Témoin Homme - Bouteille + Verre', 'Coffret bouteille + verre gravé', 24.08, 28.90, 10, 20, 'mariage');
