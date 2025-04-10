# Write your MySQL query statement below

# person id, person name, weight, turn

# bus have limit 1000 kg
# find last peron who can fit on without exceeding
# 

# order by turn
# sum of weight choosign ID of people who are <= current ID
# dont include if sum is > 1000

select t.person_name
from
(select q1.person_name, q1.turn
from queue as q1
where (
    select sum(weight) 
    from queue as q2
    where q2.turn <= q1.turn
) <= 1000) as t
order by t.turn desc
limit 1;