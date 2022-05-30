with sale_app as(
    select sale_date, sum(sold_num) app_cnt
    from sales
    where fruit='apples'
    group by 1
),
sale_org as(
    select sale_date, sum(sold_num) org_cnt
    from sales
    where fruit='oranges'
    group by 1
)
select distinct s.sale_date sale_date, app_cnt-org_cnt diff
from sales s join sale_app a using(sale_date) join sale_org o using(sale_date)
order by 1;