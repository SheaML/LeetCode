# Write your MySQL query statement below
SELECT DISTINCT
tab1.Num as 'ConsecutiveNums'
FROM
    Logs tab1,
    Logs tab2,
    Logs tab3
WHERE
    tab1.Id = tab2.Id -1
    AND tab2.Id = tab3.Id - 1
    AND tab1.Num = tab2.Num
    AND tab2.Num = tab3.Num
