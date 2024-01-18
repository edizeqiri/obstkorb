import concurrent.futures
import hashlib
import os
import subprocess
import time

import requests
import tlsh
from icecream import ic

import MACHOKE
# import ssdeep
# import tlsh
import Mongo_Connector as mongo
import SSDEEP
import STRINGS
import TLSH

ic.configureOutput(includeContext=True)


def strings(sample):
    # Combining script path and parameters in a single command
    command = ['strings', sample]

    # Running the script with parameters and capturing the output
    start_time = time.time()
    result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
    end_time = time.time()
    # The output is stored in result.stdout
    output = result.stdout
    hash = tlsh.hash(output.encode('utf-8'))

    return hash, end_time - start_time


fuzzy_hashers = [TLSH, SSDEEP, STRINGS, MACHOKE]
i = 0


def process_file(file_path, family_path, client, schema):
    if file_path.endswith(".7z"):
        return
    path = os.path.join(family_path, file_path)
    try:
        with open(path, "rb") as file_handler:
            file_content = file_handler.read()

            entry = {
                "family": family_path.split("/")[-1],
                "SHA256": hashlib.sha256(file_content).hexdigest(),
                "file_size": os.path.getsize(path),
            }

            file = {"path": path, "data": file_content}
            for hasher in fuzzy_hashers:
                fuzzy_hash, hash_time = hasher.hash(file)
                entry[hasher.__name__.lower()] = {hasher.__name__.lower(): fuzzy_hash, "hash_time": hash_time}
            file_handler.close()

            mongo.upsert_sample(client, schema, entry)

    except Exception as e:
        print(f"Error processing {path}: {e}")

def insert_family_hashes_proc(family_path, client, schema):
    file_paths = [f for f in os.listdir(family_path) if not f.startswith(".")]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        tasks = [executor.submit(process_file, file_path, family_path, client, schema) for file_path in file_paths]
        for future in concurrent.futures.as_completed(tasks):
            pass  # Process results here if needed


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
                     }

            # Machoke
            # m_fuzz, m_time = machoke_hash(file_)
            # entry["machoke"] = {"machoke": m_fuzz, "hash_time": m_time}

            # ImpFuzz
            # i_fuzz, i_time = impfuzz(file_)
            # entry["impfuzzy"] = {"impfuzzy": i_fuzz, "hash_time": i_time}

            # Strings
            # f_fuzz, f_time = strings(file_)
            # entry["strings"] = {"strings": f_fuzz, "hash_time": f_time}
            # Get fuzzy hashes and time

            # for hasher in fuzzy_hashers:
            #    fuzzy_hash, hash_time = get_fuzz_and_time_of_hasher(hasher, file_handler)
            #    entry[hasher.__name__] = {hasher.__name__: fuzzy_hash, "hash_time": hash_time}
            file_handler_.close()
            # Insert into db

            mongo.insert_one_sample(client, schema, entry)
            i += 1

        except Exception as e:
            print(f"This is some gaga: {file_}")
            print(f"The Exception is: {e}")
            if e == "DOS Header magic not found.":
                continue
            exception_counter += 1
            if exception_counter > 100:
                os.sysexit(-1)
                print("Fix your code!")
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
    print("We have {} families in the database".format(len(db[schema].distinct("family"))))


if __name__ == '__main__':
    debug = True
    start = time.time()
    path = "/Users/edi/Nextcloud/Uni/7. Semester/Bachelors_Thesis/scicore/ABySS/abyss-todot_2.0.2-goolf-1.7.20"
    print(f"Time elapsed: {time.time() - start} seconds")
