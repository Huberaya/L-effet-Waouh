-- V5 MERGE VARIANTS - Transforme produits doublons lot/couleur en variantes

-- 1. Cierges magiques lot 50 et 100 -> 1 produit avec 2 variantes
-- Garde MAR-CIERGE-020 (lot 50) comme produit parent, ajoute variante lot 100
INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty)
SELECT 
  (SELECT id FROM products WHERE sku='MAR-CIERGE-020'),
  'MAR-CIERGE-020-VAR-100',
  'Lot 100 (économie 15%)',
  'pack_qty',
  'x100',
  48.90,
  80
WHERE EXISTS (SELECT 1 FROM products WHERE sku='MAR-CIERGE-020');

-- Désactive lot 100 produit séparé (devient variante)
UPDATE products SET is_active=0 WHERE sku='MAR-CIERGE-021';

-- 2. Ballon 90cm rose/bleu déjà en variantes, mais on a 2 produits séparés? Vérifie
-- On garde GR-BAL-90-001 avec variantes rose/bleu déjà existantes

-- 3. Fumigènes lot 2 déjà variantes rose/bleu/mixte

-- 4. Canon confettis déjà variantes x1/x3/x6

-- 5. Cartes à gratter déjà variantes rose/bleu

-- 6. Kits anniversaire: licorne 70pcs et licorne 15 enfants -> garde 70pcs comme parent, 15 enfants comme variante "Complet 15 enfants"
INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty)
SELECT
  (SELECT id FROM products WHERE sku='ANN-LICORNE-200'),
  'ANN-LICORNE-200-VAR-COMPLET-15',
  'Complet 15 enfants (+vaisselle + pinata + sachets)',
  'pack_type',
  'complet-15',
  74.90,
  20
WHERE EXISTS (SELECT 1 FROM products WHERE sku='ANN-LICORNE-200');

-- Désactive kit 15 enfants séparé (devient variante)
UPDATE products SET is_active=0 WHERE sku='KIT-ANN-450';

-- 7. Bougies: 3 produits bougie ambré -> 1 produit avec variantes event + lot
-- Garde BAP-BOUGIE-300 (baptême) comme parent
INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty)
SELECT
  (SELECT id FROM products WHERE sku='BAP-BOUGIE-300'),
  'BAP-BOUGIE-300-VAR-MARIAGE-LOT10',
  'Mariage Lot 10',
  'event_pack',
  'mariage-x10',
  34.90,
  30
WHERE EXISTS (SELECT 1 FROM products WHERE sku='BAP-BOUGIE-300');

INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty)
SELECT
  (SELECT id FROM products WHERE sku='BAP-BOUGIE-300'),
  'BAP-BOUGIE-300-VAR-NAISSANCE-LOT15',
  'Naissance Lot 15',
  'event_pack',
  'naissance-x15',
  24.90,
  25
WHERE EXISTS (SELECT 1 FROM products WHERE sku='BAP-BOUGIE-300');

-- Désactive bougies mariage lot 10 et perso générique (deviennent variantes)
UPDATE products SET is_active=0 WHERE sku IN ('MAR-BOUGIE-131','PERSO-BOUGIE-502');

-- 8. Contenants dragées: verre bouchon liège lot 20 et plexi lot 20 -> garde plexi (plus moderne) avec variante verre
INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty)
SELECT
  (SELECT id FROM products WHERE sku='BAP-DRAGEE-301'),
  'BAP-DRAGEE-301-VAR-VERRE-LIEGE',
  'Verre Bouchon Liège Lot 20 (traditionnel)',
  'material',
  'verre-liege',
  16.90,
  50
WHERE EXISTS (SELECT 1 FROM products WHERE sku='BAP-DRAGEE-301');

UPDATE products SET is_active=0 WHERE sku='MAR-DRAGEES-130';

-- 9. Ballons baby shower 50pcs rose/bleu déjà, mais on a aussi kit déco 70pcs -> garde kit 70pcs comme parent complet
-- Pas de dedup supplémentaire

-- 10. Affiche naissance personnalisée et affiche perso générique -> merge
UPDATE products SET is_active=0 WHERE sku='PERSO-AFFICHE-500';

-- 11. Ballon bulle perso et ballon bulle naissance -> merge
UPDATE products SET is_active=0 WHERE sku='NAIS-BALLON-BULLE-016';

-- 12. Vaisselle baby shower 20 pers fille/garçon -> garde fille comme parent, garçon comme variante
INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty)
SELECT
  (SELECT id FROM products WHERE sku='BS-VAISSELLE-122'),
  'BS-VAISSELLE-122-VAR-GARCON',
  'Garçon Bleu Gold 20 pers',
  'color',
  'garcon-bleu',
  19.90,
  30
WHERE EXISTS (SELECT 1 FROM products WHERE sku='BS-VAISSELLE-122');

UPDATE products SET is_active=0 WHERE sku='BS-VAISSELLE-123';

-- 13. Jeux pronostics baby shower lot 20 déjà, bingo lot 20 -> garde pronostics comme parent, bingo comme variante
INSERT OR IGNORE INTO product_variants(product_id, sku, name, attribute_type, attribute_value, price_ttc, stock_qty)
SELECT
  (SELECT id FROM products WHERE sku='BS-JEU-124'),
  'BS-JEU-124-VAR-BINGO',
  'Bingo Baby Shower Lot 20',
  'game_type',
  'bingo',
  7.90,
  40
WHERE EXISTS (SELECT 1 FROM products WHERE sku='BS-JEU-124');

UPDATE products SET is_active=0 WHERE sku='BS-JEU-125';

-- Final count: 140 -> ~120 après merge variants
-- SELECT COUNT(*) FROM products WHERE is_active=1;
