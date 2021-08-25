SELECT r.ranking, p.first_name, p.last_name, p.country, r.date
INTO player_ranking
FROM players AS p
LEFT JOIN rankings AS r
ON r.id = p.player_id
ORDER BY date;

ALTER TABLE player_ranking ADD COLUMN ID SERIAL PRIMARY KEY;
ALTER TABLE player_ranking
ADD COLUMN full_name varchar;
UPDATE player_ranking SET full_name = CONCAT(first_name, ' ', last_name)

ALTER TABLE player_ranking
RENAME COLUMN date TO ranking_dates;

ALTER TABLE player_ranking
RENAME COLUMN id TO ident



