# Write your MySQL query statement below

# id email
# return wher emails are duplicates
# i could make a subquery 


select t.email
from
(
    select email, count(email) as amount
    from person
    group by email
) as t
where t.amount > 1 and t.email is not null;