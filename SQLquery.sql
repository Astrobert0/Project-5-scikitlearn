
/*rent analysis ----------------------------------------------*/
CREATE TEMPORARY TABLE rent_full
SELECT * FROM project_5.rent1
LIMIT 0 
;
INSERT INTO project_5.rent_full
SELECT *
	FROM project_5.rent2
;
INSERT INTO project_5.rent_full
SELECT *
	FROM project_5.rent1
;
SELECT ROUND(AVG(price)) AS 'AveragePrice', ROUND(AVG(size)) AS 'AverageSize', ROUND(AVG(priceByArea)) AS 'AVG_PriceByArea' FROM project_5.rent_full
;


/*sale analysis --------------------------------------------------*/
CREATE TEMPORARY TABLE sale_full
SELECT * FROM project_5.sale1
LIMIT 0 
;
INSERT INTO project_5.sale_full
SELECT *
	FROM project_5.sale2
;
INSERT INTO project_5.sale_full
SELECT *
	FROM project_5.sale1
;
SELECT ROUND(AVG(price), 3) AS 'AveragePrice', ROUND(AVG(size)) AS 'AverageSize', ROUND(AVG(priceByArea),3) AS 'AVG_PriceByArea' FROM project_5.sale_full