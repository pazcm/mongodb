import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "testDB"
COLLECTION_NAME = "firstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# new_docs = [{'first': 'popeye', 'last': 'el marino', 'dob': '13/01/28', 'hair-color': 'blonde', 'occupation': 'marino', 'nationality': 'american'},
# {'first': 'cocoliso', 'last': 'adams', 'dob': '13/03/98', 'hair-color': 'none', 'occupation': 'baby', 'nationality': 'american'}, 
# {'first': 'brutus', 'last': 'the terrible', 'dob': '1/10/38', 'hair-color': 'dark', 'occupation': 'marino', 'nationality': 'american'}]

# coll.insert_many(new_docs)

# coll.remove({'first': 'olivia'})

coll.update({'first': 'cocoliso'}, {'$set': {'last': 'bebe'}})


documents = coll.find()



for doc in documents:
    print(doc)