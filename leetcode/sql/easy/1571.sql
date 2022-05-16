select name warehouse_name, sum(width*length*height*units) volume
from warehouse join products using(product_id)
group by 1;