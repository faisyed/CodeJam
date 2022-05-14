with count_info as(
    select count(*) im_cnt
    from delivery
    where order_date=customer_pref_delivery_date
),
total_info as(
    select count(*) tot_cnt
    from delivery
)
select round((im_cnt/tot_cnt)*100,2) immediate_percentage
from count_info, total_info;