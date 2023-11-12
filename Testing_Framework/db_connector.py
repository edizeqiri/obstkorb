import pymongo


def init():
    """
    Returns db object
    """
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Create db and coll if does not exist
    if "FuzzyHashing" not in client.list_database_names():
        db = client["FuzzyHashing"]
        if "families" not in db.list_collection_names():
            db.create_collection("families")
        if "samples" not in db.list_collection_names():
            db.create_collection("samples")
    return client["FuzzyHashing"]


def insert_one_sample(client, coll, data):
    """
    Insert data into collection
    """
    if coll not in client.list_collection_names():
        print("Collection does not exist")
        return False

    client[coll].insert_one(data)
    return True


def find(client, query):
    """
    Find data in collection
    """
    if client["families"] not in client.list_collection_names():
        print("Collection does not exist! Run init() first")
        return False
    return client["families"].find(query)


# debug

#cursor = init()

#print(cursor.list_collection_names())
