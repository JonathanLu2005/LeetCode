# Write your MySQL query statement below
# sale id, product id, year, quanitiy, price
# sale id + yr = primary key
# product id = foregin key
#

# product id, product name

# want report product name, year, price
# for each sale id

select p.product_name, s.year, s.price
from sales s, product p
where s.product_id = p.product_id;