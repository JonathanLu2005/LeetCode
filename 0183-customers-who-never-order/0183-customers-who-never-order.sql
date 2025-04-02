# Write your MySQL query statement below
# id name

# id customerid

# find who never order

select name as customers
from customers
where id not in (
    select customerid
    from orders
);