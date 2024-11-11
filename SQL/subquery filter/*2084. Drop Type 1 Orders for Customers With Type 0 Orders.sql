/*
Table: Orders

+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  | 
| customer_id | int  |
| order_type  | int  | 
+-------------+------+
order_id is the column with unique values for this table.
Each row of this table indicates the ID of an order, the ID of the customer who ordered it, and the order type.
The orders could be of type 0 or type 1.
 

Write a solution to report all the orders based on the following criteria:

If a customer has at least one order of type 0, do not report any order of type 1 from that customer.
Otherwise, report all the orders of the customer.
Return the result table in any order.

The result format is in the following example.
*/

select order_id, customer_id, order_type
from Orders
where (customer_id, order_type) in
(SELECT customer_id, MIN(order_type) 
    FROM Orders 
    GROUP BY customer_id)