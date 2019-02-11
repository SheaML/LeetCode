# Write your MySQL query statement below
UPDATE 
    salary
SET 
    sex = REPLACE(REPLACE(REPLACE(sex,'f','t'),'m','f'),'t','m')
