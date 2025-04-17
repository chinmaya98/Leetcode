SELECT customer_id, COUNT(*) as count_no_trans
FROM Visits V
LEFT JOIN Transactions T on T.visit_id = V.visit_id
WHERE T.transaction_id IS NULL
GROUP BY customer_id