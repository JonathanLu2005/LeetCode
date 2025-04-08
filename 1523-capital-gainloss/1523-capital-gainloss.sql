# Write your MySQL query statement below

# stock name, operation, operation day, price

# operation is Sell or Buy

# sort operation day from 1 to whatever (asc) maybe not matter since its all gonna accumulate
# then if its buy we want to make price negative
# then we do sum, and group by stock name

select stock_name, sum(case when operation = 'Buy' then price * -1 else price end) as capital_gain_loss
from stocks
group by stock_name;
