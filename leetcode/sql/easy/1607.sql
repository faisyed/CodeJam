with orders_2020 as(
    select distinct seller_id
    from orders
    where date_format(sale_date,'%Y')='2020'
)
select seller_name
from seller
where seller_id not in (select seller_id from orders_2020)
order by 1;