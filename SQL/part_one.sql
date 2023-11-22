
-- Version simple sans prendre en compte le format de la date, avec une date dans la table au format yyyy-mm-dd
SELECT 
    date, 
    SUM(prod_price * prod_qty) AS ventes 
FROM TRANSACTIONS
WHERE YEAR(date) = 2019
GROUP BY date
ORDER BY date;



-- Version en prenant précisément les formats de l'énoncé, avec la date en string dans la table, au format jj/mm/yy
SELECT 
    DATE_FORMAT(STR_TO_DATE(date, '%d/%m/%y'), '%d/%m/%Y') AS date, 
    SUM(prod_price * prod_qty) AS ventes 
FROM TRANSACTIONS
WHERE YEAR(STR_TO_DATE(date, '%d/%m/%y')) = 2019
GROUP BY date
ORDER BY date;

