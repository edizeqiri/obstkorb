import hashlib
import subprocess
import time

import pandas as pd

import Mongo_Connector as mongo
from icecream import ic

from Playground import machoke


class MACHOKE:
    @staticmethod
    def hash(file):
        script_path = '../Playground/machoke.py'
        command = ['python', script_path, file["path"], "-v"]
        try:
            start_time = time.time()
            result = subprocess.run(command, stdout=subprocess.PIPE, text=True, check=True)
            end_time = time.time()
            output = result.stdout
        except subprocess.CalledProcessError as e:
            output = f"Error: {e}"
        return output, end_time - start_time

    @staticmethod
    def predict(file, schema, debug=False):
        db = mongo.init("portainer", port=32768)
        query = {"machoke": {"$ne": "TNULL"}}
        projection = {"family": 1, "machoke": 1, "SHA256": 1, "_id": 0}

        db_q = db[schema].find(query, projection)
        df = pd.DataFrame(db_q)
        family_counts = df['family'].value_counts()
        df = df[df['family'].map(family_counts) > 1]
        df.dropna(subset=['machoke'], inplace=True)
        df['machoke'] = df['machoke'].apply(lambda x: x['machoke'] if 'ssdeep' in x and isinstance(x, dict) else x)
        with open(file, "rb") as file_handler:
            file_content = file_handler.read()
            sha256 = hashlib.sha256(file_content).hexdigest()

        hash_sample, _ = MACHOKE.hash(file)

        max = 0
        family = "No Match!"
        #TODO: Fix this for machoke
        """for row in df.itertuples(index=False):
            try:
                if not debug:
                    if row.SHA256 == sha256:
                        continue
                if row.ssdeep == "TNULL":
                    continue
                diff_score = machoke.compare(hash_sample, row.ssdeep)
                if diff_score > max > 50:
                    min_diff = diff_score
                    family = row.family
            except Exception as e:
                print(f"Error processing row: {e}")
        ic(min_diff)"""
        return family
