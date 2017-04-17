select rating, avg(rental_duration)
from film
group by rating
having avg(rental_duration) > 5
order by rating;