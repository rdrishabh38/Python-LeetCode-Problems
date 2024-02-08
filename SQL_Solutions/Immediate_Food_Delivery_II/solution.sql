# Write your MySQL query statement below

select
ROUND((SUM(case when min_order_date = min_customer_pref_delivery_date then 1 else 0 end) / SUM(case when customer_id then 1 else 0 end)) * 100, 2) as immediate_percentage
from
(
select customer_id, min(order_date) as min_order_date, min(customer_pref_delivery_date ) as min_customer_pref_delivery_date from Delivery
group by customer_id
)x