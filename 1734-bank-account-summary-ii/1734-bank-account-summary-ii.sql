# Write your MySQL query statement below

# account, name

# transid, account, amount, transcted date
# amount pos if receive, negative if transffered
# start with 0 balance
# report name and balance with balance > 10000
# subquery ???

select u.name, m.amount as balance
from users u, 
(
    select account, sum(amount) as amount
    from transactions
    group by account
) as m
where m.amount > 10000
and u.account = m.account;