import hashlib
import time

import pandas as pd
import ssdeep
import Mongo_Connector as mongo
from icecream import ic


class SSDEEP:
    @staticmethod
    def hash(file):
        start_time = time.time()
        hash = ssdeep.hash(file["data"])
        end_time = time.time()
        return hash, end_time - start_time

    @staticmethod
    def predict(file, schema, debug=False):
        db = mongo.init("portainer", port=32768)
        query = {"ssdeep": {"$ne": "TNULL"}}
        projection = {"family": 1, "ssdeep": 1, "SHA256": 1, "_id": 0}

        db_q = db[schema].find(query, projection)
        df = pd.DataFrame(db_q)
        family_counts = df['family'].value_counts()
        df = df[df['family'].map(family_counts) > 1]
        df.dropna(subset=['ssdeep'], inplace=True)
        df['ssdeep'] = df['ssdeep'].apply(lambda x: x['ssdeep'] if 'ssdeep' in x and isinstance(x, dict) else x)
        with open(file, "rb") as file_handler:
            file_content = file_handler.read()
            hash_sample = ssdeep.hash(file_content)
            sha256 = hashlib.sha256(file_content).hexdigest()

        max = 0
        family = "No Match!"
        for row in df.itertuples(index=False):
            try:
                if not debug:
                    if row.SHA256 == sha256:
                        continue
                if row.ssdeep == "TNULL":
                    continue
                diff_score = ssdeep.compare(hash_sample, row.ssdeep)
                if diff_score > max > 50:
                    min_diff = diff_score
                    family = row.family
            except Exception as e:
                print(f"Error processing row: {e}")
        ic(min_diff)
        return family
