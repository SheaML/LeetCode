# Write your MySQL query statement below

SELECT * from cinema
WHERE id %2 !=0 AND description !='boring'
ORDER by rating DESC
