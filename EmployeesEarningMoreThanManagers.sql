# Write your MySQL query statement below

SELECT A.Name As 'Employee'
FROM Employee A, Employee B
WHERE A.ManagerID = B.Id AND A.Salary > B.Salary

