# https://pypi.org/project/pymongo/
# https://docs.mongodb.com/guides/server/insert/
from pprint import pprint

import pymongo
client = pymongo.MongoClient("host.docker.internal", 27017)
db = client.test
db.name
#u'test'


db.my_collection
#Collection(Database(MongoClient('localhost', 27017), u'test'), u'my_collection')
db.my_collection.insert_one({"x": 10}).inserted_id
#ObjectId('4aba15ebe23f6b53b0000000')
db.my_collection.insert_one({"x": 8}).inserted_id
#ObjectId('4aba160ee23f6b543e000000')
db.my_collection.insert_one({"x": 11}).inserted_id
#ObjectId('4aba160ee23f6b543e000002')
db.my_collection.find_one()
#{u'x': 10, u'_id': ObjectId('4aba15ebe23f6b53b0000000')}
for item in db.my_collection.find():
    print(item["x"])
#10
#8
#11
db.my_collection.create_index("x")
#u'x_1'
for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
    print(item["x"])
#8
#10
#11
ids = [item["x"] for item in db.my_collection.find().limit(2).skip(1)]
print(ids)
#[8, 11]


# -----


# https://docs.mongodb.com/guides/server/insert/#insert-a-single-document
db.inventory.insert_one(
    {"item": "canvas",
     "qty": 100,
     "tags": ["cotton"],
     "size": {"h": 28, "w": 35.5, "uom": "cm"}})

# https://docs.mongodb.com/guides/server/read/#retrieve-all-documents-in-the-inventory-collection
cursor = db.inventory.find({})
for inventory in cursor:
    pprint(inventory)