from pymongo import MongoClient



client = MongoClient("mongodb://localhost:27017/")

client.drop_database("football-statistics")

db = client["football-statistics"]

collection = db["players-details"]

teams_collection = db["teams-details"]

transfer_collection = db['transfer-pool']



with open("./config/players.csv", "r") as file:
    for row in file:
        new_string = row.rstrip()
        if (new_string):
            (player_team, player_name, matches, goals, assists) = new_string.split(',')
            statistics = {}
            statistics['player_team'] = player_team
            statistics['player_name'] = player_name
            statistics['matches'] = matches
            statistics['goals'] = goals
            statistics['assists'] = assists
        
        collection.insert_one(statistics)


with open("./config/teams.csv", "r") as file:
    for row in file:
        new_string = row.rstrip()
        if (new_string):
            (team_name, league_name, funds_available, supporters) = new_string.split(',')
            team_details = {}
            team_details['team-name'] = team_name
            team_details['league-name'] = league_name
            team_details['funds-available-in-billion'] = float(funds_available)
            team_details['supporters'] = supporters

        teams_collection.insert_one(team_details)


with open("./config/transfer-pool.csv", "r") as file:
    for row in file:
        new_string = row.rstrip()
        if (new_string):
            (player_in_transfer_pool, cost) = new_string.split(',')
            transfer_window_details = {}
            transfer_window_details['player-in-window'] = player_in_transfer_pool
            transfer_window_details['cost-of-player-in-billion'] = float(cost) 

        transfer_collection.insert_one(transfer_window_details)