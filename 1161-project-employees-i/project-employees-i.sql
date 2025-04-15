SELECT project_id, ROUND(SUM(experience_years)/COUNT(project_id),2) as average_years
FROM Project P
LEFT JOIN Employee E on P.employee_id = E.employee_id
GROUP BY P.project_id