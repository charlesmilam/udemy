select count(*)
from film
where rating = 'R'
and replacement_cost between 5 and 15;