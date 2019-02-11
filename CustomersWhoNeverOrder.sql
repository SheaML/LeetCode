# Write your MySQL query statement below
SELECT A.Name as 'Customers'
FROM Customers A
LEFT JOIN Orders B
ON A.Id = B.CustomerId
WHERE B.CustomerId IS NULL
