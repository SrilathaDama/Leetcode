# Write your MySQL query statement below
WITH total_employee AS (SELECT project_id, COUNT(employee_id) as total
FROM Project
GROUP BY project_id)

SELECT project_id
FROM total_employee
WHERE total = (SELECT MAX(total) FROM total_employee)