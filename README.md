# Football Manager Game
## About the game
### Console based football manager game
#### Picking your squad
In this game you have to choose your squad and compete against other teams.
In the beginning you will be presented with choices for the 4 major roles in your team: 
- goalkeeper 
- defenders
- midfielders 
- attackers 

You have to pick _1_ goalkeeper, _4_ defenders, _4_ midfielders and _2_ attackers on a turn by turn basis.

Each position will be displayed in the format **Player_Number  Player_Name - Player_Rating**.
To pick the players you want type their numbers in the console separated by whitespaces. `5 6 7 8`
#### Match Simulation
After picking your squad a match will be simulated between your team and other teams.
Your team will play against every team in the game in random order twice and after you team
has played against every team twice the cycle is repeated.

The score is determined by each team's strength and random chance.
Your team strength is determined by the rating of the players you selected earlier.
Team strength is split in two variables **team attack strength** and **team defense strength**.
Team defense strength is determined by the average strength of your goalkeeper, defenders and half of your midfielders
Team attack strength is determined by the average strength of half of your midfielders and your attackers.