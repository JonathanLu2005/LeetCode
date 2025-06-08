# Write your MySQL query statement below

# if even its id below else its id above

SELECT ROW_NUMBER() OVER() id, student
FROM seat ORDER BY IF(MOD(id, 2) = 0, id-1, id+1)