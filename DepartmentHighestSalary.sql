# Write your MySQL query statement below
SELECT  Department.Name as Department, Employee.Name as Employee, Employee.Salary as Salary
FROM Employee
    JOIN Department
    ON Employee.DepartmentId = Department.Id
WHERE
(Employee.DepartmentId, Salary) IN
(SELECT
    DepartmentId, MAX(Salary)
    FROM 
        Employee
    GROUP BY DepartmentId)
