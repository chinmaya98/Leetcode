SELECT teacher_id, COUNT(Distinct subject_id) as cnt
FROM Teacher
GROUP BY teacher_id