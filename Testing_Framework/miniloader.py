import concurrent.futures
import hashlib
import os
import time
import subprocess
from itertools import combinations

import tlsh
import json
import sys
from icecream import ic
import MACHOKE

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


fuzzy_hashers = [MACHOKE]
i = 0


def mhash(file):
    # script_path = '../Playground/machoke.py'
    script_path = 'machoke.py'
    command = ['python', script_path, file["path"], "-v"]
    try:
        start_time = time.time()
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
        end_time = time.time()
        output = result.stdout
    except subprocess.CalledProcessError as e:
        output = f"Error: {e}"
    return output, end_time - start_time


def process_file(file_path, family_path):
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
            file_handler.close()

            file = {"path": path, "data": file_content}

            fuzzy_hash, hash_time = mhash(file)
            entry["machoke"] = {"machoke": fuzzy_hash, "hash_time": hash_time}

            return entry

    except Exception as e:
        print(f"Error processing {path}: {e}")
        return entry


def insert_family_hashes_proc(family_path):
    file_paths = [f for f in os.listdir(family_path) if not f.startswith(".")]
    results = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        tasks = [executor.submit(process_file, file_path, family_path) for file_path in file_paths]
        for future in concurrent.futures.as_completed(tasks):
            try:
                results.append(future.result())
            except Exception as e:
                print(f"Operation failed: {e}")
    return results


def init(family_path, schema):
    families = os.listdir(family_path)
    results = []
    for i, family in enumerate(families):
        if family.startswith("."):
            continue
        results.extend(insert_family_hashes_proc((family_path + "/" + family).replace("/", os.sep)))

    with open('machoke_results.json', 'w') as json_file:
        json.dump(results, json_file)


if __name__ == '__main__':
    start = time.time()
    path = "/users/stud/z/zeqiri0000/scicore"
    init(path, "scicore")
    print(f"Time elapsed: {time.time() - start} seconds")
