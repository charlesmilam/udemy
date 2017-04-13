select rating, avg(replacement_cost)
from film
group by rating;