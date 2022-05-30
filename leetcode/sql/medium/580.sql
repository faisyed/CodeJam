with student_count as(
    select dept_id, count(student_id) cnt
    from student
    group by 1
)
select dept_name, ifnull(cnt, 0) student_number
from department
left join student_count using(dept_id)
order by 2 desc, 1;