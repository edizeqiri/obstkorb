import pymongo


def init():
    """
    Returns db object
    """
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    fuzzies = ["sdhash", "ssdeep", "tlsh", "machoc"]

    # Create db and coll if does not exist
    if "FuzzyHashing" not in client.list_database_names():
        db = client["FuzzyHashing"]
        for fuzz in fuzzies:
            if fuzz not in db.list_collection_names():
                db.create_collection(fuzz)
    return client["FuzzyHashing"]


def insert(client, coll, data):
    """
    Insert data into collection
    """
    if coll not in client.list_collection_names():
        print("Collection does not exist")
        return False
    if data["families"] is None or data["SHA256"] is None or data["fuzzy_hashes"] is None:
        print(f"Data is not right: {data}")
        return False

    client[coll].insert_one(data)


def find(client, coll, query):
    """
    Find data in collection
    """
    if coll not in client.list_collection_names():
        print("Collection does not exist")
        return False
    return client[coll].find(query)


# debug

cursor = init()

print(cursor.list_collection_names())
