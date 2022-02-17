
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())

mycol = mydb["customers"]

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
  
  
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
  
  
mydict = { "name": "John", "address": "Highway 37" }

#x = mycol.insert_one(mydict)


mydict = { "name": "Peter", "address": "Lowstreet 27" }

#x = mycol.insert_one(mydict)

#print(x.inserted_id)


x = mycol.find_one()

print(x)

for x in mycol.find():
  print(x)