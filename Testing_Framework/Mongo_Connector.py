import pymongo


def init(ip, port=27017):
    """
    Returns db object
    """
    client = pymongo.MongoClient(f"mongodb://{ip}:{port}/")

    # Create db and coll if does not exist
    if "FuzzyHashing" not in client.list_database_names():
        db = client["FuzzyHashing"]
        if "families" not in db.list_collection_names():
            db.create_collection("families")
        if "samples" not in db.list_collection_names():
            db.create_collection("samples")
        if "scicore" not in db.list_collection_names():
            db.create_collection("scicore")
        if "scicore_samples" not in db.list_collection_names():
            db.create_collection("scicore_samples")
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


def find(client,schema ,query):
    """
    Find data in collection
    """
    if client["families"] not in client.list_collection_names():
        print("Collection does not exist! Run init() first")
        return False
    return client[schema].find(query)

def upsert_sample(client, schema, entry):
    """
    Inserts a new document or updates an existing one based on the 'SHA256' field.

    :param client: MongoClient instance
    :param schema: The database and collection name in the format 'db.collection'
    :param entry: The document to insert or update
    """

    collection = client[schema]

    sha256 = entry.get('SHA256')
    if not sha256:
        raise ValueError("Entry does not contain 'SHA256' field")

    # Update the document with the given SHA256, or insert it if it doesn't exist
    result = collection.update_one(
        {'SHA256': sha256},
        {'$set': entry},
        upsert=True
    )

    return result


