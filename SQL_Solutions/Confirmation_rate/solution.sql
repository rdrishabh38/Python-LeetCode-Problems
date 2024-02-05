select user_id,
COALESCE(Round(((total - timeout)/total),2),0) as confirmation_rate
from
(
select s.user_id,
SUM(case when c.action = 'timeout' then 1 else 0 end)  as timeout,
SUM(case when c.action = 'timeout' or c.action = 'confirmed' then 1 else 0 end) as total
from Signups s
left Join
Confirmations c
on s.user_id = c.user_id
group by user_id
)x


--Varun solution

select user_id,round(sum(confirm)/count(1),2) as confirmation_rate from
(select s.user_id,action,case when action='confirmed' then 1 else 0 end as confirm from Signups s
left join Confirmations c on s.user_id=c.user_id)x
group by user_id