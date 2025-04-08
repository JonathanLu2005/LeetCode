# Write your MySQL query statement below

# id, p_id
# leaf, root, inner
# if P_id = null, then its root
# if id never exist as p_id, its leaf
# else inner

select id, 'Root' as type
from tree
where p_id is null 
union
select id, 'Inner' as type 
from tree
where p_id is not null and id in (select p_id from tree)
union
select id, 'Leaf' as type 
from tree
where id not in (select p_id from tree where p_id is not null)
and p_id is not null;