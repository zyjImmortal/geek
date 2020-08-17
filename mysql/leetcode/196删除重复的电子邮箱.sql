delete
from Persion
where Id NOT in(
    select need.id from (select min(Id) as id from Persion group by Email) as need
    )