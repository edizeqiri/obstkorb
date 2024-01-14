import hashlib
import subprocess
import time

import pandas as pd
import ssdeep
import tlsh

import Mongo_Connector as mongo
from icecream import ic


class STRINGS:
    @staticmethod
    def hash(file):
        # Combining script path and parameters in a single command
        command = ['strings', file]

        # Running the script with parameters and capturing the output
        start_time = time.time()
        result = subprocess.run(command, stdout=subprocess.PIPE, text=True)
        end_time = time.time()
        # The output is stored in result.stdout
        output = result.stdout
        hash = tlsh.hash(output.encode('utf-8'))

        return hash, end_time - start_time

    @staticmethod
    def predict(file, schema, debug=False):
        db = mongo.init("portainer", port=32768)
        query = {"strings": {"$ne": "TNULL"}}
        projection = {"family": 1, "strings": 1, "SHA256": 1, "_id": 0}

        db_q = db[schema].find(query, projection)
        df = pd.DataFrame(db_q)
        family_counts = df['family'].value_counts()
        df = df[df['family'].map(family_counts) > 1]
        df.dropna(subset=['strings'], inplace=True)
        df['strings'] = df['strings'].apply(lambda x: x['strings'] if 'strings' in x and isinstance(x, dict) else x)
        with open(file, "rb") as file_handler:
            file_content = file_handler.read()
            hash_sample = tlsh.hash(file_content)
            sha256 = hashlib.sha256(file_content).hexdigest()

        max = 0
        family = "No Match!"
        for row in df.itertuples(index=False):
            try:
                if not debug:
                    if row.SHA256 == sha256:
                        continue
                if row.strings == "TNULL":
                    continue
                diff_score = tlsh.diff(hash_sample, row.strings)
                if diff_score > max > 50:
                    min_diff = diff_score
                    family = row.family
            except Exception as e:
                print(f"Error processing row: {e}")
        ic(min_diff)
        return family
