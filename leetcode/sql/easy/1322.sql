select ad_id,
ifnull(round(sum(action='Clicked')/sum(action='Clicked' or action='Viewed') * 100,2),0) ctr
from ads
group by 1
order by 2 desc, 1;