SELECT empuni.unique_id, emp.name
FROM Employees emp
LEFT JOIN EmployeeUNI empuni on emp.id = empuni.id
