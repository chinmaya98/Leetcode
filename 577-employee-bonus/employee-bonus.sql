SELECT name, bonus
FROM Employee E
LEFT JOIN Bonus B on E.empID = B.empID
WHERE B.bonus < 1000 OR B.bonus IS NULL