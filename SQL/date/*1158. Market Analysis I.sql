/*
Table: Users

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| join_date      | date    |
| favorite_brand | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) of this table.
This table has the info of the users of an online shopping website where users can sell and buy items.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| order_date    | date    |
| item_id       | int     |
| buyer_id      | int     |
| seller_id     | int     |
+---------------+---------+
order_id is the primary key (column with unique values) of this table.
item_id is a foreign key (reference column) to the Items table.
buyer_id and seller_id are foreign keys to the Users table.

*/

SELECT 
  u.user_id AS buyer_id, 
  join_date, 
  COUNT(o.order_id) AS orders_in_2019 
FROM 
  Users u 
  LEFT JOIN Orders o ON u.user_id = o.buyer_id 
  and YEAR(o.order_date)= '2019' 
GROUP BY 
  u.user_id 
