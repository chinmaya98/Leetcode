# Write your MySQL query statement below
Select P.product_id, Coalesce(Round(sum(price*units)/sum(units),2),0) as average_price
from Prices P left join UnitsSold U
on P.product_id = U.product_id
And U.purchase_date between P.start_date and P.end_date
group by product_id