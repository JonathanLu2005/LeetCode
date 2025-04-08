# Write your MySQL query statement below

# user id, activity date, activity type, activity duration

# type is free trial, paid, cancelled
# duration is number minute spent on platform

# offer 7 day plan, then lead to paid or cancel

# find user who converted free to paid
# calculate average daily actiavty during free trial
# calculate user avg actiivty during paid

# so first we only care about users who paid
# then just get sum when activity type is whatever and divide by count
# and group by

# subquery, find total activity for free trial, total activity for paid and numebr day spent

#select t.user_id, t.activity duration as trial_avg_duration, t.activity_duration as paid_avg_duration
#from (select user_id, activity_type, round((sum(activity_duration) /  count(activity_type)),2) as activity_duration
#from useractivity 
#where activity_type = 'paid' or activity_type = 'free_trial'
#group by user_id, activity_type) as t
#where count(t.user_id) = 2
#group by t.activity_type;

select user_id,
    round(avg(case when activity_type = 'free_trial' then activity_duration end), 2) as trial_avg_duration,
    round(avg(case when activity_type = 'paid' then activity_duration end), 2) as paid_avg_duration
from useractivity
where activity_type in ('free_trial', 'paid')
group by user_id
having count(distinct activity_type) = 2;