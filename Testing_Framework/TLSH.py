import hashlib
import time

import pandas as pd
import tlsh
import Mongo_Connector as mongo
from icecream import ic


class TLSH:

    @staticmethod
    def hash(file):
        start_time = time.time()
        hash = tlsh.hash(file["data"])
        end_time = time.time()
        return hash, end_time - start_time

    @staticmethod
    def predict(file, schema, debug=False):
        db = mongo.init("portainer", port=32768)
        query = {"tlsh": {"$ne": "TNULL"}}
        projection = {"family": 1, "tlsh": 1, "SHA256": 1, "_id": 0}

        db_q = db[schema].find(query, projection)
        df = pd.DataFrame(db_q)
        family_counts = df['family'].value_counts()
        df = df[df['family'].map(family_counts) > 1]
        df.dropna(subset=['tlsh'], inplace=True)
        df['tlsh'] = df['tlsh'].apply(lambda x: x['tlsh'] if 'tlsh' in x and isinstance(x, dict) else x)
        with open(file, "rb") as file_handler:
            file_content = file_handler.read()
            hash_sample = tlsh.hash(file_content)
            sha256 = hashlib.sha256(file_content).hexdigest()

        min_diff = 10000
        family = "No Match!"
        for row in df.itertuples(index=False):
            try:
                if not debug:
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

