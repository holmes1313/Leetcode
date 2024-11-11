/*
Table: Customers

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| customer_id   | int     |
| name          | varchar |
+---------------+---------+
customer_id is the column with unique values for this table.
This table contains information about customers.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| customer_id   | int     |
| cost          | int     |
+---------------+---------+
order_id is the column with unique values for this table.
This table contains information about the orders made by customer_id.
Each customer has one order per day.
 

Write a solution to find the most recent three orders of each user. If a user ordered less than three orders, return all of their orders.

Return the result table ordered by customer_name in ascending order and in case of a tie by the customer_id in ascending order. If there is still a tie, order them by order_date in descending order.

The result format is in the following example.
*/
with rankedorders as (
SELECT 
        o.order_id,
        o.order_date,
        o.customer_id,
        c.name AS customer_name,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id order by o.order_date desc) as order_rank
    FROM Orders o
    JOIN Customers c ON o.customer_id = c.customer_id
)

select customer_name,
customer_id,
order_id,
order_date
from rankedorders
where order_rank <= 3
order by customer_name asc, customer_id asc, order_date desc;