
-- Première CTE pour réduire le scope des requêtes aux champs utiles et dates utiles.
WITH 
transactions_2019 AS (
    SELECT 
        client_id, 
        (prod_price * prod_qty) AS ventes,
        product_type
    FROM TRANSACTIONS 
    LEFT JOIN PRODUCT_NOMENCLATURE 
    ON prod_id = product_id
    WHERE YEAR(STR_TO_DATE(date, '%d/%m/%y')) = 2019
),

-- Calculer les ventes de meubles par client
ventes_meubles AS (
    SELECT 
        client_id,
        SUM(ventes) AS ventes_meubles
    FROM transactions_2019
    WHERE product_type = "MEUBLE"
    GROUP BY client_id
),

-- Calculer les ventes de déco par client
ventes_deco AS (
    SELECT 
        client_id,
        SUM(ventes) AS ventes_deco
    FROM transactions_2019
    WHERE product_type = "DECO"
    GROUP BY client_id
)

-- Requête faite sur MySQL en local, full join à utiliser sur BigQuery
SELECT 
    vm.client_id, 
    vm.ventes_meubles, 
    vd.ventes_deco 
FROM ventes_meubles vm
LEFT JOIN ventes_deco vd 
ON vm.client_id = vd.client_id

UNION

SELECT 
    vd.client_id, 
    vm.ventes_meubles, 
    vd.ventes_deco 
FROM ventes_meubles vm
RIGHT JOIN ventes_deco vd 
ON vm.client_id = vd.client_id;

-- Version full join non testée
/*SELECT 
    COALESCE(vm.client_id, vd.client_id) AS client_id, 
    vm.ventes_meubles, 
    vd.ventes_deco 
FROM ventes_meubles vm
FULL JOIN ventes_deco vd ON vm.client_id = vd.client_id;*/