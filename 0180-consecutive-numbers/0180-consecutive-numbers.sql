# Write your MySQL query statement below
# return value where next 2 rows are completely same, can compare 3 tables together
select distinct t1.num as ConsecutiveNums
from logs as t1, logs as t2, logs as t3
where 
t1.id + 1 = t2.id and t2.id + 1 = t3.id
and t1.num = t2.num and t2.num = t3.num;