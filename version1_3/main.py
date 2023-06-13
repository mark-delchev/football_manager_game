from flask import Flask, render_template, request
from players import Player

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def generate_player():
    if request.method == 'POST':
        picked_country = request.form['country']
        team1 = Player()
        team1.choose_country(picked_country)

        # Generate multiple players (e.g., 5 players)
        num_players = 5
        players_info = []
        for _ in range(num_players):
            player_info = team1.gen_player_info(max_rating=100, academy=False)
            players_info.append(player_info)

        return render_template('result.html', players_info=players_info, chosen_country=picked_country)
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
