select problem_id
from problems
where (likes/(likes+dislikes))*100 < 60
order by problem_id;