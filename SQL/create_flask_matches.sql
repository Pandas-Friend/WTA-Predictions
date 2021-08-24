create table flask_matches as
select m.index, m.tourney_date,  m.surface,  m.winner_name,  m.loser_name, m.winner_rank, m.loser_rank
from matches as m
order by tourney_date;