/*
Table Variables:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| name          | varchar |
| value         | int     |
+---------------+---------+
In SQL, name is the primary key for this table.
This table contains the stored variables and their values.
 

Table Expressions:

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| left_operand  | varchar |
| operator      | enum    |
| right_operand | varchar |
+---------------+---------+
In SQL, (left_operand, operator, right_operand) is the primary key for this table.
This table contains a boolean expression that should be evaluated.
operator is an enum that takes one of the values ('<', '>', '=')
The values of left_operand and right_operand are guaranteed to be in the Variables table.
 

Evaluate the boolean expressions in Expressions table.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Variables table:
+------+-------+
| name | value |
+------+-------+
| x    | 66    |
| y    | 77    |
+------+-------+
Expressions table:
+--------------+----------+---------------+
| left_operand | operator | right_operand |
+--------------+----------+---------------+
| x            | >        | y             |
| x            | <        | y             |
| x            | =        | y             |
| y            | >        | x             |
| y            | <        | x             |
| x            | =        | x             |
+--------------+----------+---------------+
Output: 
+--------------+----------+---------------+-------+
| left_operand | operator | right_operand | value |
+--------------+----------+---------------+-------+
| x            | >        | y             | false |
| x            | <        | y             | true  |
| x            | =        | y             | false |
| y            | >        | x             | true  |
| y            | <        | x             | false |
| x            | =        | x             | true  |
+--------------+----------+---------------+-------+
Explanation: 
As shown, you need to find the value of each boolean expression in the table using the variables table.
*/

select 
 e.left_operand,
    e.operator,
    e.right_operand,
    case when e.operator = '=' then
        case when lv.value = rv.value then 'true' else 'false' end
        WHEN e.operator = '>' THEN 
            CASE WHEN lv.value > rv.value THEN 'true' ELSE 'false' END
        WHEN e.operator = '<' THEN 
            CASE WHEN lv.value < rv.value THEN 'true' ELSE 'false' END
    END as value



from 
Expressions e
join Variables lv on lv.name = e.left_operand
join Variables rv on rv.name = e.right_operand