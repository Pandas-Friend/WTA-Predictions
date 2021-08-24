from flask import Flask, json, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Zaqedc12@localhost:5432/WTA"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# The dropdown values for the players names from the current players table
def get_dropdown_values():
    player_values = players.query.with_entities(players.full_name).distinct().where(
        players.ranking < 150).order_by(players.last_name)
    return player_values

# The dropdown values for the dates in the current players table
def get_dates():
    dates = players.query.with_entities(players.ranking_dates).distinct().where(
        players.ranking_dates.isnot(None)).order_by(players.ranking_dates)
    return dates

# The dropdown values for the rankings in the current players table.
def get_player_rank(player, dates):
    results = players.query.filter(players.full_name==player, players.ranking_dates==dates).first()
    return results.ranking

# The query to determine if the players played each other.
def get_match(player_a, player_b):
    #match_played = matches.query.filter((matches.winner_name==player_a & matches.loser_name==player_b) | (matches.winner_name==player_b & matches.loser_name==player_a)).first()
    a_won = matches.query.filter(matches.winner_name==player_a, matches.loser_name==player_b).first()
    b_won = matches.query.filter(matches.winner_name==player_b, matches.loser_name==player_a).first()
    if (a_won is not None):
        text_output =  "{} ranked {} won over {} ranked {} on {}".format(a_won.winner_name,a_won.winner_rank,a_won.loser_name,a_won.loser_rank, a_won.tourney_date)
        return text_output
    elif (b_won is not None):
        text_output = "{} ranked {} won over {} ranked {} on {}".format(b_won.winner_name,b_won.winner_rank,b_won.loser_name,b_won.loser_rank, b_won.tourney_date)
        return text_output
    else:
        return "These players haven't played each other"


# Player Ranking table 
class players(db.Model):
    __tablename__ = 'player_ranking'

    ranking = db.Column(db.Integer)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    country = db.Column(db.String())
    ranking_dates = db.Column(db.Integer())
    ident = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String())

    def __init__(self, ranking, first_name, last_name, country, ranking_dates, ident, full_name):
        self.ranking = ranking
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.ranking_dates = ranking_dates
        self.id = ident
        self.full_name = full_name

    def __repr__(self):
        return f"<Player {self}>"

# Matches table
class matches(db.Model):
    __tablename__ = 'flask_matches'

    index = db.Column(db.Integer, primary_key=True)
    tourney_date = db.Column(db.Integer())
    surface = db.Column(db.String())
    winner_name = db.Column(db.String())
    loser_name = db.Column(db.String())
    winner_rank = db.Column(db.Integer())
    loser_rank = db.Column(db.Integer())

    def __init__(self, index, tourney_date, surface, winner_name, loser_name, winner_rank, loser_rank):
        self.index = index
        self.tourney_date = tourney_date
        self.surface = surface
        self.winner_name = winner_name
        self.loser_name = loser_name
        self.winner_rank = winner_rank
        self.loser_rank = loser_rank

    def __repr__(self):
        return f"<Matches {self}>"

# Once the user selects the players, surface and date the players ranking is obtained and the whether the players played each other and output to the index page.
@app.route('/_process_data')
def process_data():
    selected_player_a = request.args.get('selected_player_a', type=str)
    selected_player_b = request.args.get('selected_player_b', type=str)
    selected_date = request.args.get('selected_date', type=str)	
    player_a_rank = get_player_rank(selected_player_a, selected_date)
    player_b_rank= get_player_rank(selected_player_b, selected_date)
    if (player_a_rank < player_b_rank):
        winner = selected_player_a
        loser = selected_player_b
    else:
        winner = selected_player_b
        loser = selected_player_a
    
    recent_winner = get_match(selected_player_a, selected_player_b)

    return jsonify(random_text="On the WTA tour on {} {} was ranked {} and {} was ranked {}.  If they played on that day {} would win over {} based on the machine learning model predicition of 63.5 percent.  {}.".format(selected_date, selected_player_a, player_a_rank, selected_player_b, player_b_rank, winner, loser, recent_winner))

# Set up for the the index page with drop down values for players and dates.
@app.route("/")
def index():
    values = get_dropdown_values()
    date_value = get_dates()
    return render_template("index.html", player_a=values, player_b=values, dates=date_value)


if __name__ == '__main__':
    app.run(debug=True)
