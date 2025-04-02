# Write your MySQL query statement below
# product id, product name, desc
# return with valid serial
# serial is 4 digits - 4 digits
# return ascending order with product id

select * from products
where description REGEXP 'SN[0-9]{4}-[0-9]{4}$'
or description regexp 'SN[0-9]{4}-[0-9]{4}[^0-9]+'
order by product_id asc;