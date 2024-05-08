Question Source : https://datalemur.com/blog/atlassian-sql-interview-questions

SQL Question 1: Average Bug Resolutions Time by Teams

Atlassian provides products like JIRA that helps keep track of tasks, bugs and issues among other features. Assume you have two tables, teams and bugs. The teams table contains information about each team and its team_id, and the bugs table contains information about each bug, its bug_id, the team who resolved it and the start and resolution date.


The objective is to write a SQL query to calculate the average resolution time for bugs for each team.

teams Example Input:

team_id	team_name
1	Team Alpha
2	Team Bravo
3	Team Charlie

bugs Example Input:

bug_id	team_id	created_at	resolved_at
1	1	2018-06-09 00:00:00	2018-06-12 00:00:00
2	1	2018-06-10 00:00:00	2018-06-15 00:00:00
3	2	2018-06-11 00:00:00	2018-06-13 00:00:00
4	2	2018-06-12 00:00:00	2018-06-16 00:00:00
5	3	2018-06-13 00:00:00	2018-06-15 00:00:00



SQL Fiddle MYSQL queries :

-- INIT database

create table teams(
  team_id INT,
  team_name varchar(100)
  );

CREATE TABLE bugs (
  bug_id INT,
  team_id INT,
  created_at timestamp,
  resolved_at timestamp
);
INSERT INTO teams VALUES (1,'Team Alpha');
INSERT INTO teams VALUES (2, 'Team Bravo');
INSERT INTO teams VALUES (3, 'Team Charlie');

insert into bugs values(1,1,'2018-06-09 00:00:00','2018-06-12 00:00:00');
insert into bugs values(2,1,'2018-06-10 00:00:00','2018-06-15 00:00:00');
insert into bugs values(3,2,'2018-06-11 00:00:00','2018-06-13 00:00:00');
insert into bugs values(4,2,'2018-06-12 00:00:00','2018-06-16 00:00:00');
insert into bugs values(5,3,'2018-06-13 00:00:00','2018-06-15 00:00:00');