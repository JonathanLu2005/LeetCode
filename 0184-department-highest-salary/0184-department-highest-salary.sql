# Write your MySQL query statement below

# employee: id, name, salary, department id

# department: id, name

# find employees with highest salary in each department

# filter by max salary and department id

# lets join first

# need to get use to the id of using tuples and checking if its in x y z, easiest way to do like a for loop ish

select d.name as Department, e.name as Employee, e.salary as Salary
from department d, employee e
where e.departmentId = d.id
and (e.departmentId, salary) 
in (select departmentId, max(salary) from employee group by departmentId);