from pymongo import MongoClient

client = MongoClient("localhost", 27017)
gobDb = client["GoBDB"]
jobCollection = gobDb["Jobs"]

categories = jobCollection.aggregate([
    {
        '$project': {
            'category': '$attributes.category_name',
            'title': '$attributes.title'
        }
    }
])

print(list(categories))