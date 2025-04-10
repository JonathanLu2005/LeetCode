# Write your MySQL query statement below

# select salaries which are < max salary
# then select max salary

select max(salary) as SecondHighestSalary
from employee e
where e.salary < (select max(salary) from employee);