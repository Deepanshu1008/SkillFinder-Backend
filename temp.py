import pymongo
from dotenv import load_dotenv

load_dotenv()
from bson.objectid import ObjectId

import os
MONGO_URI = os.environ.get('MONGO_URI')
client = pymongo.MongoClient(MONGO_URI)
db = client["SkillFinder"]
def read(db, collection, query):
    return db[collection].find(query)
def read_one(db, collection, query):
    return db[collection].find_one(query)
def create(db, collection, data):
    return db[collection].insert_one(data)
def update(db, collection, query, data):
    return db[collection].update_one(query, data)
def delete(db, collection, query):
    return db[collection].delete_one(query)
create(db,'users',{'name':"Deepanshu"})
