from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:GoBrewers12@localhost:5432/WTA"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


def get_dropdown_values():
    player_values = players.query.with_entities(players.full_name).distinct().where(
        players.ranking < 150).order_by(players.last_name)
    return player_values


def get_dates():
    dates = players.query.with_entities(players.ranking_dates).distinct().where(
        players.ranking_dates.isnot(None)).order_by(players.ranking_dates)
    return dates

def get_player(player, dates):
    return players.query.with_entities(players.ranking).where(players.full_name==player).where(players.ranking_dates==dates)

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


@app.route('/_process_data')
def process_data():
    selected_player_a = request.args.get('selected_player_a', type=str)
    selected_player_b = request.args.get('selected_player_b', type=str)
    selected_surface = request.args.get('selected_surface', type=str)
    selected_date = request.args.get('selected_date', type=str)	
    player1 = get_player(selected_player_a, selected_date)
    return jsonify(random_text="You selected {} and {} for date of {} on a {} surface {}".format(selected_player_a, selected_player_b, selected_date, selected_surface, player1))

@app.route("/")
def index():
    values = get_dropdown_values()
    date_value = get_dates()
    return render_template("index.html", player_a=values, player_b=values, dates=date_value)


if __name__ == '__main__':
    app.run(debug=True)
