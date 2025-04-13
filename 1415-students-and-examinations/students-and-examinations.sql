SELECT st.student_id, student_name, su.subject_name, count(ex.student_id) AS attended_exams
FROM Students st
JOIN Subjects su
LEFT JOIN Examinations ex ON st.student_id = ex.student_id AND su.subject_name = ex.subject_name
GROUP BY st.student_id, su.subject_name
ORDER BY St.student_id, su.subject_name