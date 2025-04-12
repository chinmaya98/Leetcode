SELECT customer_id, count(*) as count_no_trans
FROM Visits as V
LEFT JOIN Transactions as T on V.visit_id = T.visit_id
WHERE T.transaction_id is NULL
GROUP BY customer_id