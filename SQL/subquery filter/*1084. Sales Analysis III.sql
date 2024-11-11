/*
select p.product_id, p.product_name
from Product p 
where p.product_id not in (
select distinct product_id
from Sales
where sale_date not between '2019-01-01' and '2019-03-31' )
 and p.product_id  in (
select distinct product_id
from Sales
where sale_date  between '2019-01-01' and '2019-03-31' )
*/
