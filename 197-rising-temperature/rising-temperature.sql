SELECT a.Id
FROM Weather a
JOIN Weather b ON DateDiff(a.recordDate, b.recordDate) = 1
WHERE a.temperature > b.temperature