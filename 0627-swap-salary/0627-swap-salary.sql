# Write your MySQL query statement below
# id, name, sex, salary
# update m to f

update salary
set sex = if(sex = 'm', 'f', 'm');