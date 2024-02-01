import json
from pymongo import MongoClient

# Connect to MongoDB (adjust the connection string as needed)
client = MongoClient('mongodb://portainer:32768/')
db = client['FuzzyHashing']
collection = db['mnm']

print(db.list_collection_names())

# Load your JSON file
with open('machoke_results_malware.json', 'r') as file:
    data = json.load(file)  # This loads the entire JSON array as a Python list

# Filter out None values if your array contains them
filtered_data = [item for item in data if item is not None]
print(filtered_data[1])
# Insert into the collection
if filtered_data:  # Ensure there's data to insert
    collection.insert_many(filtered_data)
