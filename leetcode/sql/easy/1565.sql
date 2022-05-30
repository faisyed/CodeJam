select date_format(order_date,"%Y-%m") month, count(distinct order_id) order_count, count(distinct customer_id) customer_count
from orders
where invoice>20
group by 1;