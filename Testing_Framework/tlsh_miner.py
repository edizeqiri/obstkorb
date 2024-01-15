import numpy as np
import pandas as pd
import Mongo_Connector as mongo
import tlsh
from icecream import ic
import matplotlib.pyplot as plt
import ssdeep
import warnings
from concurrent.futures import ProcessPoolExecutor
from itertools import combinations

from tmp import subresult

db = mongo.init("portainer", port=32768)
df = pd.DataFrame(list(db["malware"].find({})))

family_counts = df['family'].value_counts()
malware_filtered = df[df['family'].map(family_counts) > 1]
malware_filtered = malware_filtered.dropna()

malware_filtered["scicore"] = False
size = malware_filtered.shape[0] / 20
scicore = pd.DataFrame(list(db["scicore"].aggregate([{"$sample": {"size": size}}])))
scicore["scicore"] = True

malware_concat = pd.concat([malware_filtered, scicore])

a = malware_concat
a = a[a['tlsh'] != 'TNULL']
a.dropna(subset=['tlsh'], inplace=True)
a.dropna(subset=['ssdeep'], inplace=True)
a.dropna(subset=['strings'], inplace=True)

a = a[a['tlsh'] != 'TNULL']

a['tlsh'] = a['tlsh'].apply(lambda x: x['tlsh'] if 'tlsh' in x and isinstance(x, dict) else x)
a = a[a['tlsh'] != 'TNULL']
a['ssdeep'] = a['ssdeep'].apply(lambda x: x['ssdeep'] if 'ssdeep' in x and isinstance(x, dict) else x)

a['strings'] = a['strings'].apply(lambda x: x['strings'] if 'strings' in x and isinstance(x, dict) else x)
a = a[a['strings'] != 'TNULL']
filtered_df = a



def subresult(frame):
    local_result = []

    for i in range(len(frame)):
        min_score = 10000
        winner = []
        score = 100000
        for j in range(len(numi)):
            if frame[i][3] == numi[j][3]:
                continue
            try:
                score = tlsh.diff(frame[i][0], numi[j][0])
            except:
                print(f"Error in tlsh: {frame[i][1]} and {numi[j][1]}, {frame[i][2]} and {numi[j][2]}, ")
                break
            if score < min_score:
                min_score = score
                winner = [frame[i][1], numi[j][1], frame[i][2], numi[j][2], score]
        local_result.append(winner)
    return local_result


def tlsh_score(df, col="tlsh"):
    numi = df[[col, 'family', 'scicore', 'SHA256']].to_numpy()
    batch = 200
    total_batches = len(range(0, len(numi), batch))
    results = []
    completed_batches = 0

    with concurrent.futures.ProcessPoolExecutor(max_workers=32) as executor:
        future_results = [executor.submit(subresult, numi[i:i + batch], numi) for i in range(0, len(numi), batch)]
        for future in concurrent.futures.as_completed(future_results):
            try:
                results.extend(future.result())
            except Exception as e:
                print(f"Operation failed: {e}")
    return results
