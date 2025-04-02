# Write your MySQL query statement below

# id name

# id salary

# return id where missing info

select t.employee_id
from
(
    select * from employees left join salaries using(employee_id)
    union
    select * from employees right join salaries using(employee_id)
) as t
where t.salary is null or t.name is null
order by employee_id;