# Write your MySQL query statement below
SELECT MAX(Salary) AS SecondHighestSalary FROM Employee 
WHERE SALARY NOT IN (SELECT MAX(SALARY) FROM Employee)
