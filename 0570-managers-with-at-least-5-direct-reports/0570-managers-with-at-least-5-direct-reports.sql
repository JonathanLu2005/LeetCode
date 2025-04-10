# Write your MySQL query statement below

# id, name, department, manager id

# manager with >= 5 direct reports
# basically when their id has been used >= 5 times

select e1.name 
from employee e1
where (select count(*) from employee e2 where e2.managerId = e1.id) >= 5;
