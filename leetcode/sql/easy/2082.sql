select count(distinct customer_id) rich_count
from store
where amount>500
having count(distinct bill_id)>1;