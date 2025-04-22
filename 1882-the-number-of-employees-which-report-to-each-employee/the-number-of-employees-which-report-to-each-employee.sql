SELECT e.employee_id, e.name, count(emp.reports_to) as reports_count, round(avg(emp.age)) as average_age
from Employees e inner join employees emp on e.employee_id = emp.reports_to
group by employee_id
order by employee_id 