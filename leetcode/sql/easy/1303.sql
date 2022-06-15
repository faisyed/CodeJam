with team_info as(
    select team_id, count(employee_id) as team_size
    from employee
    group by team_id
)
select employee_id,team_size
from employee e join team_info t using(team_id)
order by 1;