with max_cnt as(
    select count(*) cnt
    from friends
    group by activity
    order by 1 desc
    limit 1
),
min_cnt as(
    select count(*) cnt
    from friends
    group by activity
    order by 1
    limit 1
)
select activity
from friends
group by 1
having count(*)>(select cnt from min_cnt) and count(*)<(select cnt from max_cnt);