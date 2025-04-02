# Write your MySQL query statement below
# tweet id, content
# invalid if > 15

select tweet_id
from tweets
where length(content) > 15;