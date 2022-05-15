with red_sales as(
    select sales_id
    from orders join company using(com_id)
    where name='RED'
)
select name
from salesperson
where sales_id not in(select sales_id from red_sales);