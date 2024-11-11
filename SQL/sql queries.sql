
-- Window function
 SUM(amount) OVER (ORDER BY date ROWS BETWEEN 1 PRECEDING AND current row) AS rolling_sum
 avg(amount) over (order by visited_on range between interval 6 day preceding and current row)
ROW_NUMBER() OVER (PARTITION BY o.customer_id order by o.order_date desc) as order_rank

-- IFNULL
 IFNULL(SUM(distance),0) AS travelled_distance

 -- String functions
 concat(upper(substring(name, 1, 1)),lower(substring(name, 2))) as name
 CHAR_LENGTH(content)> 15
 mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*\\@leetcode\\.com$';