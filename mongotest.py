import pymongo

client = pymongo.MongoClient("mongodb+srv://sambit035:sambit03513@sambit035.zdgvx.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "Sambit",
    "email " : "paulsambit2@gmail.com",
    "surname" : "paul"
}


db1 = client['mangotest']
coll = db1['test']
coll.insert_one(d)