select * from matches;
select * from rankings;
select * from players;

select ranking
into player_ranking
from rankings as r
left join players as p 
on p.player_id = r.player_id
order by ranking;

select * from player_ranking;


