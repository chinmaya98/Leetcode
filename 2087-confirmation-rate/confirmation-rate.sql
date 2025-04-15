SELECT S.user_id, ROUND(AVG(CASE WHEN C.action='confirmed' THEN 1 ELSE 0 END), 2) as confirmation_rate
FROM Signups S
LEFT JOIN Confirmations C on S.user_id = C.user_id
GROUP BY S.user_id