import hashlib
import os
import time

import requests
import ssdeep
import tlsh
import Playground.machoke as machoke
import sdhash
import db_connector as mongo
import json
import sys
from icecream import ic
ic.configureOutput(includeContext=True)



# TODO: implement Machoke
fuzzy_hashers = [ssdeep, tlsh]



def get_fuzz_and_time_of_hasher(hasher, file_handler):
    start_time = time.time()
    fuzz = hasher.hash(file_handler)
    end_time = time.time()
    return fuzz, end_time - start_time


def get_hash(hasher, fuzz, client):
    result = mongo.find(client, hasher, {hasher: {"fuzzy_hash": fuzz}})
    return result.family


def insert_family_hashes(family_path, client):
    for file in os.listdir(family_path.replace("/", os.sep)):
        # if file has .7z ending skip
        if file.endswith(".7z"):
            continue

        # Get file information
        file_ = (family_path + "/" + file).replace("/", os.sep)

        try:
            file_handler_ = open(file_, "rb")
            file_handler = file_handler_.read()
            sample_data = {"family": family_path.split("/")[-1],
                           "SHA256": hashlib.sha256(file_handler).hexdigest(),
                           "file_size": os.path.getsize(file_),
                           "ssdeep": "ssdeep hash",
                           "sdhash": "sdhash hash",
                           "tlsh": "TLSH hash",
                           "machoc": "Machoc hash"}

            # Get fuzzy hashes and time
            for hasher in fuzzy_hashers:
                fuzzy_hash, hash_time = get_fuzz_and_time_of_hasher(hasher, file_handler)
                sample_data[hasher.__name__] = {hasher.__name__: fuzzy_hash, "hash_time": hash_time}
            file_handler_.close()
            # Insert into db
            mongo.insert_one_sample(client, "families", sample_data)
        except Exception as e:
            print(f"This is some gaga: {file_}")
            print(f"The Exception is: {e}")
            continue


    return True


def log_me(data):
    if requests.get("https://ntfy.airfryer.rocks/").status_code == 200:
        requests.post("https://ntfy.airfryer.rocks/dev", data=data)

def init(family_path):
    db = mongo.init("portainer", port=32768)
    log_me("Starting init phase")
    for i, family in enumerate(os.listdir(family_path)):
        if family.startswith("."):
            continue
        log_me(f"{family} is being processed. {i}/{len(family_path)}")
        insert_family_hashes((family_path + "/" + family).replace("/", os.sep), db)

    log_me(f"Finished processing {len(family_path)} families")
    print("We have {} families in the database".format(len(db.list_collection_names())))

def test():
    Rat9002_1 = open("Samples/006c74c6813a6efeabea860b2718ed548eed216a319d76ceb178fc38cba458d1", 'rb').read()
    Rat9002_1 = ic(tlsh.hash(Rat9002_1))
    Rat9002_2 = open("Samples/0414ffdf9dcf32061cc57d0b54bf4410c1c588258c12615988e3ce8cb0cf4fb4", 'rb').read()
    Rat9002_2 = ic(tlsh.hash(Rat9002_2))
    AgentTesla = open("Samples/0f9e27ec1ed021fd7375ca46f233c06b354d12d57aed44132208cd9308bfee11", 'rb').read()
    AgentTesla = ic(tlsh.hash(AgentTesla))
    ic(tlsh.diff(Rat9002_1, Rat9002_2))
    ic(tlsh.diff(Rat9002_1, AgentTesla))
    ic(tlsh.diff(Rat9002_2, AgentTesla))

if __name__ == '__main__':
    # if len(sys.argv) < 3:
    #     print("Usage: python3 Tester.py <path_to_families> <True/False> for init phase") #make this a flag
    #     exit(1)
    #
    #
    # family_path = sys.argv[1]
    # if sys.argv[2] == "True":
    #     init(family_path)
    #

    init("/Volumes/vx")