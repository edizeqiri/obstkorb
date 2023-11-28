import hashlib
import os
import time

import requests
import ssdeep
import tlsh
import Playground.machoke as machoke
import sdhash
import Mongo_Connector as mongo
import json
import sys
from icecream import ic

ic.configureOutput(includeContext=True)

# TODO: implement Machoke
fuzzy_hashers = [ssdeep, tlsh]
i = 0

def get_fuzz_and_time_of_hasher(hasher, file_handler):
    start_time = time.time()
    fuzz = hasher.hash(file_handler)
    end_time = time.time()
    return fuzz, end_time - start_time


def get_hash(hasher, sha, client):
    result = mongo.find(client, {hasher: {"SHA256": sha}})
    return result.family


def insert_family_hashes(family_path, client, schema):
    global i
    exception_counter = 0
    for file in os.listdir(family_path.replace("/", os.sep)):
        # if file has .7z ending skip
        if file.endswith(".7z"):
            continue

        # Get file information
        file_ = (family_path + "/" + file).replace("/", os.sep)

        try:
            file_handler_ = open(file_, "rb")
            file_handler = file_handler_.read()
            entry = {"_id": i,
                     "family": family_path.split("/")[-1],
                     "SHA256": hashlib.sha256(file_handler).hexdigest(),
                     "file_size": os.path.getsize(file_),
                     "ssdeep": "ssdeep hash",
                     "sdhash": "sdhash hash",
                     "tlsh": "TLSH hash",
                     "machoc": "Machoc hash"}

            # Get fuzzy hashes and time
            for hasher in fuzzy_hashers:
                fuzzy_hash, hash_time = get_fuzz_and_time_of_hasher(hasher, file_handler)
                entry[hasher.__name__] = {hasher.__name__: fuzzy_hash, "hash_time": hash_time}
            file_handler_.close()
            # Insert into db

            mongo.insert_one_sample(client, schema, entry)
            i += 1

        except Exception as e:
            print(f"This is some gaga: {file_}")
            print(f"The Exception is: {e}")
            exception_counter += 1
            if exception_counter > 100:
                os.sysexit(-1)
            else:
                continue

    return True


def log_me(data):
    if requests.get("https://ntfy.airfryer.rocks/").status_code == 200:
        requests.post("https://ntfy.airfryer.rocks/dev", data=data)


def init(family_path, schema):
    db = mongo.init("portainer", port=32768)
    log_me("Starting init phase")
    families = os.listdir(family_path)
    for i, family in enumerate(families):
        if family.startswith("."):
            continue
        if i % 10 == 0:
            log_me(f"{family} is being processed. {i}/{len(families)}")
        insert_family_hashes((family_path + "/" + family).replace("/", os.sep), db, schema)

    log_me(f"Finished processing {len(family_path)} families")
    print("We have {} Schemas in the database".format(len(db.list_collection_names())))


if __name__ == '__main__':
    # if len(sys.argv) < 3:
    #     print("Usage: python3 Loader.py <path_to_families> <True/False> for init phase") #make this a flag
    #     exit(1)
    #
    #
    # family_path = sys.argv[1]
    # if sys.argv[2] == "True":
    #     init(family_path)
    #

    #init("/Users/edi/Nextcloud/Uni/7. Semester/Bachelors_Thesis/scicore", "scicore")
    print("Hello")