select project_id
from project
group by 1
having count(employee_id) = (
    select count(employee_id)
    from project
    group by project_id
    order by count(employee_id) desc
    limit 1
);