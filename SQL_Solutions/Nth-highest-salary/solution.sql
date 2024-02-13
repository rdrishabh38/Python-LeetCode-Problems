CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
With CTE1 as
(select salary, dense_rank() over (order by salary desc) as rnk from employee)
select IFNULL((select CTE1.salary from CTE1 where CTE1.rnk = N limit 1), NULL) as  SecondHighestSalary from CTE1 limit 1
  );
END
