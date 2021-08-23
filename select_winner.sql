select * from player_ranking
where date between 
and (winner_name = 'Serena Williams'
or loser_name = 'Serena Williams')
order by winner_rank asc