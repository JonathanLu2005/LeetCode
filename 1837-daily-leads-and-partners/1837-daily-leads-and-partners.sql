# Write your MySQL query statement below
# we have date, make name (product sold), lead, partner
# for each date and product, find number of distinct lead and partner

select date_id, make_name, count(distinct(lead_id)) as unique_leads, count(distinct(partner_id)) as unique_partners
from dailysales
group by date_id, make_name;