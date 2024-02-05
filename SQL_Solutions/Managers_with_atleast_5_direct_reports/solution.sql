select e.name from
(select managerId  from
(
    select managerId , count(managerId ) as cnt from Employee group by managerId
)x where cnt >= 5
) a join Employee e on a.managerId = e.id

--Varun Mishra Solution

select e1.name from Employee e1
inner join Employee e2 on e1.id=e2.managerId
group by e2.managerId
having count(e2.managerId) >=5