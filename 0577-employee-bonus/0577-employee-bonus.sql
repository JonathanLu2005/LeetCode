# Write your MySQL query statement below
# empid, name, supervisor, salary

# empid, bonus

# report name and bonus of each employee wit bonus < 1000

select e.name, b.bonus
from employee e left join bonus b
on e.empId = b.empId
where b.bonus < 1000 or b.bonus is null;