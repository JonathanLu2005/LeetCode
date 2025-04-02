# Write your MySQL query statement below
# user ids, time stamp

# return latest login for 2020 for all users

select user_id, max(time_stamp) as last_stamp
from logins
where time_stamp like '2020%'
group by user_id;