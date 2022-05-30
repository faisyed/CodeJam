with vote_info as(
    select candidateId, count(id) cnt
    from vote
    group by 1
    order by 2 desc
    limit 1
)
select name
from candidate c join vote_info v on c.id=v.candidateId;