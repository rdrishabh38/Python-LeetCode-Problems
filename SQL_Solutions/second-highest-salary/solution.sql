--Create table If Not Exists Employee (id int, salary int)
--Truncate table Employee
--insert into Employee (id, salary) values ('1', '100')
--insert into Employee (id, salary) values ('2', '200')
--insert into Employee (id, salary) values ('3', '300')
--
--
--

-- via subquery
select max(salary) as SecondHighestSalary from  Employee where salary <
(
select max(salary)  from Employee
);

-- via CTE
With CTE1 as
(select salary, dense_rank() over (order by salary desc) as rnk from employee)
select IFNULL((select CTE1.salary from CTE1 where CTE1.rnk = 2), NULL) as  SecondHighestSalary from CTE1 limit 1;
