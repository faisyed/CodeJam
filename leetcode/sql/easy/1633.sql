with total_info as(
    select count(*) tot_count
    from users
)
select contest_id, round(count(distinct user_id)/tot_count * 100,2) percentage
from total_info, register
group by contest_id
order by 2 desc, 1;