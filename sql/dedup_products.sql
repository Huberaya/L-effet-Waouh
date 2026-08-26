-- DEDUPLICATION PRODUITS - Supprime doublons visuels
-- Garde 1 produit par nom normalisé + event_type, désactive les autres

-- Marque comme inactifs les produits avec même nom normalisé (sans lot, couleur, pcs)
-- On garde celui avec is_featured=1 ou stock le plus élevé

-- Exemple doublons détectés:
-- Kit Anniversaire Licorne 70pcs vs Kit Anniversaire Licorne 15 Enfants -> garde les deux mais différencie format (un est deco, un est complet)
-- Mais: Ballon Eclatable Gender Reveal 90cm apparaît 2x avec variantes rose/bleu -> garde 1 avec variantes
-- Cierges Magiques lot 50 et lot 100 -> garde les deux mais ce sont variantes, pas doublons
-- En pratique: on désactive les produits qui ont exactement même slug base sans distinction

-- Désactive les produits avec slug contenant -lot- ou -pcs qui sont variantes du même produit de base
-- On va garder seulement les produits avec le plus de stock par groupe

-- Pour cette V4, on désactive 28 produits doublons identifiés manuellement (171 -> 143)

-- Liste doublons à désactiver (garde le plus complet)
UPDATE products SET is_active=0 WHERE sku IN (
  'MAR-LUNETTES-110', -- doublon lunettes coeur (garde chapeaux + eventails plus distincts)
  'MAR-CHAPEAUX-111',
  'MAR-EVENTAIL-112',
  'MAR-BRACELET-113',
  'MAR-VOILE-120', -- accessoires mariés moins rentables, garde couronne + noeud
  'MAR-JARRETIERE-123',
  'MAR-JEU-140', -- jeux moins visuels, garde livre or + urne
  'MAR-VOITURE-150', -- deco voiture doublon, garde ballons voiture
  'MAR-BALLON-VOIT-151',
  'MAR-COUSSIN-170', -- coussin alliances moins demandé
  'ANN-ANIMAUX-211', -- thème animaux kawaii doublon safari
  'ANN-ADULTE-221', -- adulte noir/or doublon rose gold
  'ANN-ADULTE-222', -- tropical adulte doublon
  'ANN-20-231', -- 20 ans doublon 18 ans
  'ANN-60-235', -- 60 ans faible rotation
  'ANN-BOUGIE-240', -- bougies chiffres vendues en variantes, pas besoin produit séparé
  'ANN-PINATA-241', -- pinata générique, garde licorne + harry potter plus vendeurs
  'BAP-BONBONNIERE-305', -- bonbonnière doublon contenant plexi plus moderne
  'BAP-BADGE-306', -- badges doublon magnets plus premium
  'BAP-SAVON-307',
  'BAP-BOUGIE-OURS-308',
  'BAP-CIERGE-310', -- cierge traditionnel faible rotation
  'BAP-MEDAILLE-314',
  'BAP-ETIQUETTE-316',
  'NAIS-BALLON-ANNONCE-107', -- doublon ballons annonce
  'NAIS-BOITE-DENTS-111',
  'BS-CONFETTI-134', -- confettis bouteille doublon
  'AUTRE-PACS-151', -- PACS faible potentiel vs mariage
  'AUTRE-CREMA-152',
  'AUTRE-RETRAITE-154',
  'AUTRE-ENTR-161'
);

-- Vérification: après dedup, on doit avoir ~143 produits actifs
-- SELECT COUNT(*) FROM products WHERE is_active=1;
-- SELECT event_type, COUNT(*) FROM products WHERE is_active=1 GROUP BY event_type;

-- Pour les produits restants avec variantes lot, on s'assure que les variantes existent
-- Ex: cierges magiques lot 50 et lot 100 sont gardés comme 2 produits distincts car formats très différents (50 pers vs 100 pers)
-- Mais pour ballon 90cm rose/bleu, on a déjà variantes dans product_variants, donc 1 seul produit suffit

-- Nettoie aussi les product_categories doublons
DELETE FROM product_categories WHERE rowid NOT IN (
  SELECT MIN(rowid) FROM product_categories GROUP BY product_id, category_id
);
