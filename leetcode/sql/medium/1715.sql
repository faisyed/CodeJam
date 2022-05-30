select sum(case when b.chest_id is not null then b.apple_count+c.apple_count else b.apple_count end) apple_count, 
sum(case when b.chest_id is not null then b.orange_count+c.orange_count else b.orange_count end) orange_count
from boxes b left join chests c using(chest_id);