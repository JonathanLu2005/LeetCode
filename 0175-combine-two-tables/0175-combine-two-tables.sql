# Write your MySQL query statement below

# person id, last name, first name

# address id, person id, city, state

# report first name, last name, city, state
# address doesnt exist return null

select p.firstName, p.lastName, a.city, a.state
from person p left join address a
on p.personId = a.personId;