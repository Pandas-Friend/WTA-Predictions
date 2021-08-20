from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:GoBrewers12@localhost:5432/WTA"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

def get_dropdown_values():
    player_values = players.query.with_entities(players.full_name).distinct().where(players.ranking < 150).order_by(players.last_name)
    return player_values

def get_dates():
    dates = players.query.with_entities(players.date).distinct().where(players.date.isnot(None))
    return dates

class players(db.Model):
    __tablename__ = 'player_ranking'

    ranking = db.Column(db.Integer)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    country = db.Column(db.String())
    date = db.Column(db.Integer())
    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.String())

    def __init__(self, ranking, first_name, last_name, country, date, id, full_name):
        self.ranking = ranking
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.date = date
        self.id = id
        self.full_name = full_name

    def __repr__(self):
        return f"<Player {self}>"


@app.route('/_process_data')
def process_data():
    selected_player_a = request.args.get('selected_player_a', type=str)
    selected_player_b = request.args.get('selected_player_b', type=str)
    selected_surface = request.args.get('selected_surface', type=str)
    selected_date = request.args.get('selected_date', type=str)

    # process the two selected values here and return the response; here we just create a dummy string

    return jsonify(random_text="You selected players {} and {} on a {} surface on {}".format(selected_player_a, selected_player_b, selected_surface, selected_date))

@app.route("/")
def index():
      values = get_dropdown_values()
      dates = get_dates()
      return render_template("index.html", player_a=values, player_b=values, dates=dates)


if __name__ == '__main__':
    app.run(debug=True)