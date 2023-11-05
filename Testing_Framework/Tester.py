# Per family
#   go into the family folder
#   for every file fill the dict with the paramters from my documentation
#   return the dict
import hashlib
import os
import time
import ssdeep
import tlsh
import machoc
import sdhash
import db_connector as mongo
import json
import sys

fuzzy_hashers = ["ssdeep", "tlsh", "machoc", "sdhash"]


def get_fuzz_and_time_of_hasher(hasher, file_path):
    start_time = time.time()
    fuzz = hasher(open(file_path, 'rb').read()).hexdigest()
    end_time = time.time()
    return (fuzz, end_time - start_time)


def predictor(hasher, fuzz, client):
    result = mongo.find(client, hasher, {"fuzzy_hash": fuzz})
    return result.family


def get_file_hashes(family_path, client):
    for file in os.listdir(family_path):
        # TODO: check "Samples" folder

        # TODO: implement hashers
        # Get file information
        sample_data = {"family": family_path.split("/")[-1],
                       "SHA256": hashlib.sha256(open(family_path + "/" + file, 'rb').read()).hexdigest(),
                       "file_size": os.path.getsize(family_path + "/" + file),
                       "ssdeep": "ssdeep hash",
                       "sdhash": "sdhash hash",
                       "tlsh": "TLSH hash",
                       "machoc": "Machoc hash"}

        # Get fuzzy hashes
        for hasher in fuzzy_hashers:
            fuzzy_hash, hash_time = get_fuzz_and_time_of_hasher(hasher, family_path + "/" + file)
            sample_data[hasher] = {hasher: fuzzy_hash, "hash_time": hash_time}

        # Insert into db
        mongo.insert_one_sample(client, sample_data)
    return True


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 Tester.py <path_to_families> ")
        exit(1)

    db = mongo.init()
    family_path = sys.argv[1]
    amount = [1, 2, 3, 4, 5]

    for family in family_path:
        sample_data = get_file_hashes(family_path, amount)

    print(sample_data)
