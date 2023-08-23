from model import TransferWindow, Teams, Players


#This class is used to initailize object of Teams, Player and Transfer Window
class TransferWindowService:
    
    def __init__(self) -> None:
        self._team_coll = Teams()
        self._transfer_coll = TransferWindow()
        self._player_details = Players()

    def find_by_name(self, team_name):
        return self._team_coll.find_by_name(team_name)
    
    def find_player_in_tranfer_window(self, player_name):
        return self._transfer_coll.find_by_name(player_name)

    #This function is used to transfer funds of team to a player in the pool
    #The funds of team get reduced and player gets added to player-details collection
    def transfer_player(self, team_name, player_name):
        team_intrested = self.find_by_name(team_name)
        player_available = self.find_player_in_tranfer_window(player_name)
        print(team_intrested)
        print(player_available)

        if team_intrested is None or player_available is None:
            return "Invalid team or player name."

        funds_available = team_intrested["funds-available-in-billion"]
        cost_of_player = player_available["cost-of-player-in-billion"]
        print(funds_available)
        print(cost_of_player)


        if funds_available >= cost_of_player:
            # Calculate the updated funds for the team and set it in the database
            updated_funds = funds_available - cost_of_player
            self._team_coll.update(team_intrested,{"$set":{"funds-available-in-billion": updated_funds}})

            # Update the new document of a player to the player-details collections
            new_document = {}
            new_document['player-team'] = team_name
            new_document['player-name'] = player_name
            new_document['matches'] = int(0) 
            new_document['goals'] = int(0)
            new_document['assists'] = int(0)

            self._player_details.insert(new_document)

            # Delete the entry of player from the transfer pool collection
            self._transfer_coll.delete(player_available)




            return "Transfer successful."
        else:
            return "Insufficient funds for the transfer."



        