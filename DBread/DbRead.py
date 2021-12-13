from pymongo import MongoClient
import requests

#connect to DB and table
client = MongoClient("localhost", 27017)
gobDb = client["GoBDB"]
companiesColl = gobDb["Companies"]
jobsColl = gobDb["Jobs"]

url = "https://www.getonbrd.com"
path = "/api/v0/companies"
perPageLimit = "100"
i = 1
params = {'per_page': perPageLimit, 'page':i}

response = requests.get(url + path, params=params).json()

print("requesting company data")
while (response['data']):
    companiesColl.insert_many(response['data'])
    i = i + 1
    params = {'per_page': perPageLimit, 'page':i}
    response = requests.get(url + path, params=params).json()
print("done requesting company data")

url = "https://www.getonbrd.com"
path = "/api/v0/search/jobs"
perPageLimit = "100"
for company in companiesColl.find({}, {'attributes.name': 1}):
    i = 1
    name = company['attributes']['name']
    params = {
        'query': '"' + name + '"',
        'per_page': perPageLimit, 
        'page': i,
        'expand': '["tenant_city","modality","seniority","tags","company"]'
    }

    response = requests.get(url + path, params=params).json()

    print("requesting jobs for company " + name)
    while (response['data']):
        jobsColl.insert_many(response['data'])
        i = i + 1
        params = {
            'query': name,
            'per_page': perPageLimit, 
            'page': i,
            'expand': '["tenant_city","modality","seniority","tags","company"]'
        }
        response = requests.get(url + path, params=params).json()
    print("done requesting jobs for " + name)