import numpy as np
import pandas as pd
import Mongo_Connector as mongo
import tlsh
from icecream import ic
import matplotlib.pyplot as plt
import ssdeep
import warnings
import concurrent.futures
from itertools import combinations
import json
import sys

path_to_json="/mnt/c/Users/edi/Downloads/malware.json"

"""db = mongo.init("portainer", port=32768)
df = pd.DataFrame(list(db["malware"].find({})))"""

# load json data into dataframe
#df = pd.read_json(path_to_json)

with open(path_to_json, 'r') as file:
    data = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(data)

print(f"Length of df: {len(df)}")
family_counts = df['family'].value_counts()
malware_filtered = df[df['family'].map(family_counts) > 1]
print(f"Length of malware_filtered: {len(malware_filtered)}")
malware_filtered["scicore"] = False
size = malware_filtered.shape[0] / 20
#scicore = pd.DataFrame(list(db["scicore"].aggregate([{"$sample": {"size": size}}])))
scicore = "/mnt/c/Users/edi/Downloads/scicore.json"

with open(scicore, 'r') as file:
    data = json.load(file)

# Convert to DataFrame
scicore = pd.DataFrame(data)


#scicore = pd.read_json(scicore)

# concat only 5% of scicore to malware_filtered
scicore = scicore.sample(frac=0.05)
scicore["scicore"] = True

malware_concat = pd.concat([malware_filtered, scicore])
print(f"Length of malware_concat: {len(malware_concat)}")
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

print(f"Length of filtered_df: {len(filtered_df)}")
print(filtered_df.head())


def get_tlsh_score(stringi):
    start = stringi.find("tlsh=") + len("tlsh=")
    end = stringi.find(",", start)
    tlsh_substring = stringi[start:end]
    return tlsh_substring
    
def subresult(frame, numi):
    local_result = []

    for i in range(len(frame)):
        min_score = 10000
        winner = []
        score = 100000
        for j in range(len(numi)):
            if frame[i][3] == numi[j][3]:
                continue
            try: 
                a = get_tlsh_score(frame[i][0])
                b = get_tlsh_score(numi[j][0])
                if a == "TNULL" or b == "TNULL":
                    continue
                score = tlsh.diff(a,b)
            except:
                print(f"Error in tlsh: {frame[i][1]} and {numi[j][1]}, {frame[i][2]} and {numi[j][2]}, {frame[i][0]} and {numi[j][0]}, {a} and {b}")
                print(f"Error: {sys.exc_info()[0]}" )
                sys.exit(1)
                
            if score < min_score:
                min_score = score
                winner = [frame[i][1], numi[j][1], frame[i][2], numi[j][2], score]
        local_result.append(winner)
    return local_result


def tlsh_score(df, col="tlsh"):
    numi = df[[col, 'family', 'scicore', 'SHA256']].to_numpy()
    print(f"Length of numi: {len(numi)}")
    batch = 200
    total_batches = len(range(0, len(numi), batch))
    results = []
    completed_batches = 0

    """with concurrent.futures.ProcessPoolExecutor() as executor:
        future_results = [executor.submit(subresult, numi[i:i + batch], numi) for i in range(0, len(numi), batch)]
        for future in concurrent.futures.as_completed(future_results):
            try:
                results.extend(future.result())
            except Exception as e:
                print(f"Operation failed: {e}")"""
    

    for i in range(0, len(numi), batch):
        results.extend(subresult(numi[i:i + batch], numi))
        completed_batches += 1
        print(f"Completed {completed_batches} of {total_batches} batches")
        print(f"Lenght of results: {len(results)}")
        print(results[-1])
        break
    return results

results = tlsh_score(filtered_df)
print(len(results))

# save results to csv
results_df = pd.DataFrame(results, columns=['Family 1', 'Family 2', 'Scicore 1', "Scicore 2", 'TLSH 1', 'TLSH 2', 'Diff Score'])
results_df.to_csv("tlsh_results.csv")


