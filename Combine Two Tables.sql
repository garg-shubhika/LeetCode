# Write your MySQL query statement below
SELECT p.firstName,p.lastName,
CASE WHEN p.personId = a.personId THEN a.city ELSE Null END AS city,
CASE WHEN p.personId = a.personId THEN a.state ELSE Null END AS state
from Person p
LEFT join Address a
on a.personId = p.personId
