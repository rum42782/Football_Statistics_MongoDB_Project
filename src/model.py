from database import Database

from bson.objectid import ObjectId

class Players:
    PLAYER_COLLECTION = 'players-details'

    def __init__(self) -> None:
        self._db = Database()
        self._latest_error = ''

    @property
    def latest_error(self):
        return self._latest_error
    
    #Finds the document based on name of player
    def find_by_name(self, player_name):
        key = {'player_name' : player_name}
        return self.__find(key)
    
    # Finds a document based on the unique auto-generated MongoDB object id
    def find_by_object_id(self, obj_id):
        key = {'_id': ObjectId(obj_id)}
        return self.__find(key)
    
    #This is a base function for all find operations
    def __find(self, key):
        user_document = self._db.get_single_data(Players.PLAYER_COLLECTION, key)
        return user_document
    
    #This is used to insert the document in the player-details collection
    def insert(self, key):
        new_inserted_data = self._db.insert_single_data(Players.PLAYER_COLLECTION, key)

class Teams:
    TEAMS_COLLECTIONS = 'teams-details'

    def __init__(self) -> None:
        self._db = Database()
        self._latest_error = ''

    @property
    def latest_error(self):
        return self._latest_error
    
    #Finds the document based on name of team
    def find_by_name(self, team_name):
        key = {'team-name' : team_name}
        return self.__find(key)

    # Finds a document based on the unique auto-generated MongoDB object id
    def find_by_object_id(self, obj_id):
        key = {'_id': ObjectId(obj_id)}
        return self.__find(key)
    
    #This is a base function for all find operations
    def __find(self, key):
        user_document = self._db.get_single_data(Teams.TEAMS_COLLECTIONS, key)
        return user_document
    
    #This function is used to update the team funds after paying to player in transfer window
    def update(self, filter_criteria, data):
        user_document = self._db.update(Teams.TEAMS_COLLECTIONS, filter_criteria, data)
        return user_document

class TransferWindow:
    Transfer_Collections = 'transfer-pool'

    def __init__(self) -> None:
        self._db = Database()
        self._latest_error = ''
    
    @property
    def latest_error(self):
        return self._latest_error
    
    #Finds the document based on name of player in window
    def find_by_name(self, player_name):
        key = {'player-in-window' : player_name}
        return self.__find(key)
    
    # Finds a document based on the unique auto-generated MongoDB object id
    def find_by_object_id(self, obj_id):
        key = {'_id': ObjectId(obj_id)}
        return self.__find(key)

    #This is a base function for all find operations
    def __find(self, key):
        user_document = self._db.get_single_data(TransferWindow.Transfer_Collections, key)
        return user_document

    #This function is used to delete the entry after the transfer is completed
    def delete(self, data):
        deleted_data = self._db.delete(TransferWindow.Transfer_Collections, data)
        return deleted_data

    
