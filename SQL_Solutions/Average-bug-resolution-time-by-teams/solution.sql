--TIMESTAMPDIFF() function
--
--MySQL the TIMESTAMPDIFF() returns a value after subtracting a datetime expression from another.
--
--It is not necessary that both the expression are of the same type. One may be a date and another is datetime. A date value is treated as a datetime with a default time part '00:00:00'. The unit for the result is given by another argument.
--
--The unit should be one of the following : FRAC_SECOND (microseconds), SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER, or YEAR.

--Syntax :
--
--TIMESTAMPDIFF(unit,datetime_expr1,datetime_expr2);
--
--
--mysql> SELECT TIMESTAMPDIFF(MONTH,'2009-05-18','2009-07-29');
--+------------------------------------------------+
--| TIMESTAMPDIFF(MONTH,'2009-05-18','2009-07-29') |
--+------------------------------------------------+
--|                                              2 |
--+------------------------------------------------+
--1 row in set (0.00 sec)

--select team_id, sum(difference) as total_difference, count(team_id) as total_count from
--(
--    select team_id, timestampdiff(DAY,created_at, resolved_at) as difference from bugs
--)a
--group by team_id
--
--team_id	total_difference	total_count
--1	8	2
--2	6	2
--3	2	1

select a.team_name, b.average_resolution_time from teams a inner join
(
select team_id, round(sum(difference)/count(team_id),2) as average_resolution_time from
(
    select team_id, timestampdiff(DAY,created_at, resolved_at) as difference from bugs
)a
group by team_id
)b on a.team_id = b.team_id;

--Above query will give response  :
--
--team_name	average_resolution_time
--Team Alpha	4.00
--Team Bravo	3.00
--Team Charlie	2.00

-- Solution given on website :

--Here's a possible PostgreSQL query to solve this:

SELECT
    t.team_name,
    AVG(EXTRACT(EPOCH FROM (b.resolved_at - b.created_at)))/3600 AS average_resolution_time_hours
FROM
    bugs b
JOIN
    teams t
ON
    b.team_id = t.team_id
GROUP BY
    t.team_name
ORDER BY
    average_resolution_time_hours;