from pymongo import MongoClient

def __get_db_handle():
    client = MongoClient("localhost", 27017)
    db_handle = client['GoBDB']
    return db_handle, client

def get_categories():
    (gobDb, client) = __get_db_handle()
    jobCollection = gobDb["Jobs"]

    features = jobCollection.aggregate([
        {
            '$project': {
                'category': '$attributes.category_name',
            }
        }
    ])

    return [*features]

# features = jobCollection.aggregate([
#     {
#         '$project': {
#             'category': '$attributes.category_name',
#             'title': '$attributes.title',
#             'tags': '$attributes.tags.data',
#             'seniority': '$attributes.seniority.data.attributes.name'
#         }
#     }
# ])
