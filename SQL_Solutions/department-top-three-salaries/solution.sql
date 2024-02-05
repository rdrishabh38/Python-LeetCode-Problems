Select
    b.name as Department,
    a.name as Employee ,
    a.salary as Salary
from
    (
        select * from
            (
                select  name,
                        salary,
                        departmentId,
                        dense_rank() over (partition by departmentid order by salary desc) as salary_ranked
                        from employee
            )x
        where x.salary_ranked <= 3) a
join DEPARTMENT b on a.departmentid = b.id