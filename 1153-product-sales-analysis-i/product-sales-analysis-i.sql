SELECT product_name, year, price 
FROM Sales S
LEFT JOIN Product P on S.product_id = P.product_id