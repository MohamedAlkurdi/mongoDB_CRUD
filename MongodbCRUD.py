from pymongo import MongoClient

connection_string = "mongodb://localhost:27017/"
database_string = "Homework_Demo_Database"
collection_string = "data"

client = MongoClient(connection_string)
db = client[database_string]
collection = db[collection_string]

documents = [
    {"userId": "0", "name": "ali", "age": 19, "employeed": False},
    {"userId": "1", "name": "ahmet", "age": 25, "employeed": True},
    {"userId": "2", "name": "cuma", "age": 28, "employeed": True},
    {"userId": "3", "name": "gülsün", "age": 37, "employeed": True},
    {"userId": "4", "name": "halit", "age": 14, "employeed": False},
    {"userId": "5", "name": "muna", "age": 44, "employeed": True},
]

def init_collection():
    for document in documents:
        collection.insert_one(document)

def add_document(name=None, age=None, employeed=None):
    added_id = len(documents)
    new_document = {"userId": str(added_id), "name": name, "age": age, "employeed": employeed}
    collection.insert_one(new_document)

def read_document(index):
    return collection.find_one({"userId": index})

def update_document(id, name=None, age=None, employeed=None):
    updated_document = documents[int(id)]
    updated_name = name if name else updated_document["name"]
    updated_age = age if age else updated_document["age"]
    updated_employeed = employeed if employeed else updated_document["employeed"]
    replacement_document = {"userId": str(id), "name": updated_name, "age": updated_age, "employeed": updated_employeed}
    collection.replace_one({"userId": str(id)}, replacement_document)

def delete_document(id):
    collection.delete_one({"userId": str(id)})


# init_collection()

# delete_document(0)

# update_document(3, name='john doe', age=99, employeed=None)

add_document(name="numan", age="200", employeed=True)