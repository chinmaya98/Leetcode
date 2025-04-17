SELECT w1.Id
FROM Weather w1
JOIN Weather w2 ON DateDiff(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature