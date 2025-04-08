# Write your MySQL query statement below

# user id, time stamp
# sign up time

# user id, time stamp, action
# action is confirmed or timeout
# user had to confirm and it either confrimed or timeout

# confirmation rate = number request / number confirmed
# if didnt request, is 0

# i think we need to join both
# first confirmations make it so given an user id, we've their confirmation rate
# then join with sign up
# and if its null we do 0, else give number

# get average if actions confirmed (1) else 0 and join
select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from signups as s
left join confirmations as c
on s.user_id = c.user_id
group by user_id;