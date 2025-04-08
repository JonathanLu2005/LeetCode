# Write your MySQL query statement below


# account id, income

# categorise accounts, if its low salary < 20000
# average salary is 20000-50000
# high salary is > 50000
# else 0

# new idea, just create 3 tables and union them, 
# embrace idea of using set operators between tables
# use fixed constants columns!

select 'Low Salary' as category, count(account_id) as accounts_count
from accounts
where income < 20000
union
select 'Average Salary' as category, count(account_id) as accounts_count
from accounts
where income >= 20000 and income <= 50000
union
select 'High Salary' as category, count(account_id) as accounts_count
from accounts
where income > 50000;