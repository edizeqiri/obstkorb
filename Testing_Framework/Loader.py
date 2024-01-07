import concurrent.futures
import hashlib
import os
import time
import subprocess
from itertools import combinations

import requests
import tlsh
import pandas as pd
# import ssdeep
# import tlsh
import Mongo_Connector as mongo
import json
import sys
from icecream import ic

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


fuzzy_hashers = []
i = 0


def get_fuzz_and_time_of_hasher(hasher, file_handler):
    start_time = time.time()
    fuzz = hasher.hash(file_handler)
    end_time = time.time()
    return fuzz, end_time - start_time


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
                # ... other hash operations ...
            }

            # Strings
            fuzzy_hash, hash_time = strings(path)
            entry["strings"] = {"strings": fuzzy_hash, "hash_time": hash_time}

            # Machoke
            # m_fuzz, m_time = machoke_hash(path)
            # entry["machoke"] = {"machoke": m_fuzz, "hash_time": m_time}

            file_handler.close()
            # Insert into database (modify as needed)
            mongo.upsert_sample(client, schema, entry)
            # mongo.insert_one_sample(client, schema, entry)

    except Exception as e:
        print(f"Error processing {path}: {e}")


def insert_family_hashes_conc(family_path, client, schema):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        file_paths = [f for f in os.listdir(family_path) if not f.startswith(".")]
        # Create a list of tasks for the executor
        tasks = [executor.submit(process_file, file_path, family_path, client, schema) for file_path in file_paths]

        # Wait for all tasks to complete (optional, if you need to process results)
        for future in concurrent.futures.as_completed(tasks):
            pass  # You can process results here if needed


def machoke_hash(sample) -> str:
    script_path = '../Playground/machoke.py'
    command = ['python', script_path, sample, "-v"]
    try:
        start_time = time.time()
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
        end_time = time.time()
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e}"
    return output, end_time - start_time


def insert_family_hashes_proc(family_path, client, schema):
    file_paths = [f for f in os.listdir(family_path) if not f.startswith(".")]
    with concurrent.futures.ProcessPoolExecutor() as executor:
        tasks = [executor.submit(process_file, file_path, family_path, client, schema) for file_path in file_paths]
        for future in concurrent.futures.as_completed(tasks):
            pass  # Process results here if needed


# Call insert_family_hashes_conc with appropriate arguments

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


def get_tlsh_prediciton(sample, debug=False):
    db = mongo.init("portainer", port=32768)
    query = {"tlsh": {"$ne": "TNULL"}}
    projection = {"family": 1, "tlsh": 1, "SHA256": 1, "_id": 0}

    db_q = db["scicore"].find(query, projection)

    df = pd.DataFrame(db_q)
    df.dropna(subset=['tlsh'], inplace=True)
    df['tlsh'] = df['tlsh'].apply(lambda x: x['tlsh'] if 'tlsh' in x and isinstance(x, dict) else x)
    with open(sample, "rb") as file_handler:
        file_content = file_handler.read()
        hash_sample = tlsh.hash(file_content)
        sha256 = hashlib.sha256(file_content).hexdigest()

    min_diff = 10000
    family = "No Match!"
    for row in df.itertuples(index=False):
        try:
            if debug:
                if row.SHA256 == sha256:
                    continue
            if row.tlsh == "TNULL":
                continue
            diff_score = tlsh.diff(hash_sample, row.tlsh)
            if diff_score < min_diff and diff_score < 150:
                min_diff = diff_score
                family = row.family
        except Exception as e:
            print(f"Error processing row: {e}")
    ic(min_diff)
    return family
    """def process_chunk(chunk):
        min = 10000
        for row1, row2 in combinations(chunk.itertuples(index=False), 2):
            try:
                diff_score = tlsh.diff(row1.strings, row2.strings)
                if diff_score < min:
                    min = diff_score
            except Exception as e:
                print(f"Error processing row: {e}")
                continue
        return min

    # Initialize an empty list to store all results
    all_results = []

    # Iterate over the DataFrame in chunks
    for start in range(0, len(df), 100):
        end = start + 100
        chunk = df.iloc[start:end]
        all_results.extend(process_chunk(chunk))
    return min(all_results)"""


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
    # init("/Users/edi/Nextcloud/Uni/7. Semester/Bachelors_Thesis/scicore", "scicore")
    # init("E:\\Cloud\\Nextcloud\\Uni\\7. Semester\\Bachelors_Thesis\\scicore\\", "scicore")
    # init("/Volumes/vx", "malware")
    debug = True
    start = time.time()
    path = "/Users/edi/Nextcloud/Uni/7. Semester/Bachelors_Thesis/scicore/ABySS/abyss-todot_2.0.2-goolf-1.7.20"
    ic(get_tlsh_prediciton(path, debug))
    print(f"Time elapsed: {time.time() - start} seconds")
