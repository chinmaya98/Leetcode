SELECT unique_id, name
FROM Employees Emp
LEFT JOIN EmployeeUNI EMU on Emp.id = EMU.id 
