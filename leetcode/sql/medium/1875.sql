with uniq_id as(
    select employee_id
    from employees
    group by salary
    having count(*)=1
)
select employee_id, name, salary, dense_rank()
over(order by salary) team_id
from employees
where employee_id not in (select employee_id from uniq_id)
order by 4, 1;