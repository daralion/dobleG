from pymongo import MongoClient

client = MongoClient("localhost", 27017)
gobDb = client["GoBDB"]
jobCollection = gobDb["Jobs"]

categories = jobCollection.find({}, {'attributes.category_name': 1})

print(list(categories))