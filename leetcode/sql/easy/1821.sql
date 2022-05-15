with revenue_info as(
    select customer_id, year, sum(revenue) tot_revenue
    from customers
    group by customer_id, year
)
select customer_id
from revenue_info
where tot_revenue>0 and year=2021;