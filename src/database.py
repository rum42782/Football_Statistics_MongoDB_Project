from pymongo import MongoClient



class Database:
    
    DB_NAME = "football-statistics"

    def __init__(self):
        self._db_conn = MongoClient("mongodb://localhost:27017/")
        self._db = self._db_conn[Database.DB_NAME]

    # This method finds a single document using field information provided in the key parameter
    # It assumes that the key returns a unique document. It returns None if no document is found    
    def get_single_data(self, collection, key):
        db_collection = self._db[collection]
        document = db_collection.find_one(key)
        return document
    
    # This method finds multple documents based on the key provided
    def get_mutiple_data(self, collection, key):
        db_collection = self._db[collection]
        documents = db_collection.find(key)
        return documents
    
    # This method inserts the data in a new document. It assumes that any uniqueness check is done by the caller
    def insert_single_data(self, collection, data):
        db_collection = self._db[collection]
        document = db_collection.insert_one(data)
        return document.inserted_id
    
    # This method inserts muliple documents. data should be a list of multiple dicts with keys already set as attributes
    def insert_multiple_data(self, collection, data):
        db_collection = self._db[collection]
        result = db_collection.insert_many(data)
        return result.inserted_ids
    
    #This method is used to update documents in collections
    def update(self, collection, filter_criteria, data):
        db_collection = self._db[collection]
        document = db_collection.update_one(filter_criteria ,data)
        return document.modified_count
    
    def delete(self, collection, data):
        db_collection = self._db[collection]
        document = db_collection.delete_one(data)
        return document.deleted_count
