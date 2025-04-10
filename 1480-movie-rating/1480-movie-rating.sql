# Write your MySQL query statement below

# movie id, title

# user id, name

# movie id, user id, rating, created t

# find user name who has rated most movies and choose min user name
# find movie name with highest avreage rating in feb 2020, choose smallest movie

# 2 separate tables, then union

# if in a bad place, rmbr can use order by and limit
# to "sort"


# find movie with highest average in feb 2020
# filter movie by 2020 feb
# then get avg of rating group by movie id
# then join with movie name
# then order by desc, limit 1, take min

(select name as results
from
(select user_id, count(user_id) as count
from movierating
group by user_id) as t
join
users u 
on t.user_id = u.user_id
order by t.count desc, name
limit 1)

union all

(select title as results
from
(select movie_id, avg(rating) as rating
from movierating
where year(created_at) = 2020 and month(created_at) = 2
group by movie_id) as y
join movies m
on m.movie_id = y.movie_id
order by rating desc, title
limit 1);