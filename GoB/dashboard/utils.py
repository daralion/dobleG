from pymongo import MongoClient
def get_db_handle(db_name, host, port, username, password):

 client = MongoClient("localhost", 27017)
 db_handle = client['GoBDB']
 return db_handle, client