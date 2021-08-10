select p.first_name, p.last_name, p.country, r.ranking, r.date
into player_ranking
from players as p
left join rankings as r
on r.player_id = p.player_id
order by date;

select * from player_ranking;




