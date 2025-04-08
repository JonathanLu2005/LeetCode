# Write your MySQL query statement below

# customer id, product key

# product key

# report customer id if they bought all products

# select customer
# where distinct count product key
# same as count product key
# aka they bought all!

select customer_id
from customer
group by customer_id
having count(distinct product_key) = (select count(product_key) from product);