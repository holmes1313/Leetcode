/*
Table: Traffic

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| activity      | enum    |
| activity_date | date    |
+---------------+---------+
This table may have duplicate rows.
The activity column is an ENUM (category) type of ('login', 'logout', 'jobs', 'groups', 'homepage').
 

Write a solution to reports for every date within at most 90 days from today, the number of users that logged in for the first time on that date. Assume today is 2019-06-30.

Return the result table in any order.

The result format is in the following example.
*/

select login_date, count(*) as user_count
from (
select user_id, min(activity_date) as login_date
from Traffic
where activity = 'login'
group by user_id ) t1
where datediff('2019-06-30', login_date) <= 90
group by login_date