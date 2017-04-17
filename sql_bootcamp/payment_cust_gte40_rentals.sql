select customer_id, count(rental_id)
from payment
group by customer_id
having count(rental_id) >= 40
order by customer_id;