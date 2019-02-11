# Write your MySQL query statement below
SELECT class from courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
