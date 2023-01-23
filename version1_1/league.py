# Create a list of dictionaries representing the teams
teams = [
    {"name": "Manchester United", "points": 30, "goals": 20, "goal_difference": 5},
    {"name": "Liverpool", "points": 28, "goals": 25, "goal_difference": 8},
    {"name": "Chelsea", "points": 27, "goals": 22, "goal_difference": 6},
    {"name": "Manchester City", "points": 25, "goals": 21, "goal_difference": 3},
    {"name": "Tottenham", "points": 30, "goals": 29, "goal_difference": 1},
]

# Sort the teams by points in descending order
teams = sorted(teams, key=lambda x: (x["points"], x["goal_difference"]), reverse=True)

# Print the table
print("{:<20} {:>10} {:>10} {:>10}".format("Team", "Points", "Goals", "Goal Diff"))
for team in teams:
    print("{:<20} {:>10} {:>10} {:>10}".format(team["name"], team["points"], team["goals"], team["goal_difference"]))

