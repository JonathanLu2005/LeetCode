# Write your MySQL query statement below

# name continent area population gdp

# big iff
# area >= 3 million
# poplation >= 25 million


select name, population, area
from world
where population >= 25000000
or area >= 3000000;