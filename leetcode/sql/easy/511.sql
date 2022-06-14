select player_id, min(event_date) first_login
from activity
group by 1
order by 1;