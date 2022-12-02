team1_win = int(input("What is the win probablility of team 1 in percent? "))
if len(str(team1_win)) > 2:
    print("Invalid input")
else:
    team2_win = int(input("What is the win probablility of team 2 in percent? "))
    if len(str(team2_win)) > 2:
        print("Invalid input")
    else:
        team1_win = team1_win / 120
        team2_win = team2_win / 120
        team1_goals = team1_win / 0.12
        team1_goals = round(team1_goals)
        team2_goals = team2_win / 0.12
        team2_goals = round(team2_goals)
        print("Team 1 might score " + str(team1_goals) + " goals")
        print("Team 2 might score " + str(team2_goals) + " goals")
        print("Result should be: " + str(team1_goals) + " - " + str(team2_goals))