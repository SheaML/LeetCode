# Write your MySQL query statement below
SELECT Trips.Request_at AS 'Day', ROUND(((SUM(Trips.Status='cancelled_by_driver') + SUM(Trips.Status='cancelled_by_client')) / count(Trips.Status)),2) as 'Cancellation Rate'
FROM Trips
JOIN Users
ON Trips.Client_ID = Users.Users_Id
AND Users.Banned = 'No'
WHERE Trips.Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at
