with max_info as(
    select departmentId, max(salary) max_sal
    from employee
    group by 1
)
select d.name department, e.name employee, e.salary salary
from employee e join department d on d.id=e.departmentId
join max_info m on d.id=m.departmentId
where e.departmentId=m.departmentId and e.salary=m.max_sal;