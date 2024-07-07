# Write your MySQL query statement below

SELECT name as Employee from Employee E
WHERE salary>(SELECT salary from Employee Y where E.managerId=Y.id);
