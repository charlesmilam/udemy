select staff_id, count(staff_id), sum(amount)
from payment
group by staff_id;