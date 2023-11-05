# Testing Framework

This document will display how the testing should be done. Work in progress, therefore changes can occur.

## Concept

1. Create a hash for each sample
2. Save them into mongoDB
3. Sample 5 times from 1-5 of each family
4. Go through all of the data and hash with all the hashers
5. Save the results into mongoDB

## Database Schema

I will create 2 collections in MongoDB. One with the hashes of all the fuzzy hashers and one with the sampled ones.



```json
{
    "family": "Name of the family",
    "SHA256": "SHA256 of the sample",
    "file_size": "Size of the sample",
    "ssdeep": {
      "hash_time" : "Time it took to hash the sample",
      "fuzzy_hash": "Fuzzy hash of the sample",
      "prediction": "Prediction of the sample"},
    "sdhash": {
      "hash_time" : "Time it took to hash the sample",
      "fuzzy_hash": "Fuzzy hash of the sample",
      "prediction": "Prediction of the sample"} ,
    "TLSH": {
      "hash_time" : "Time it took to hash the sample",
      "fuzzy_hash": "Fuzzy hash of the sample",
      "prediction": "Prediction of the sample"} ,
    "Machoc": {
      "hash_time" : "Time it took to hash the sample",
      "fuzzy_hash": "Fuzzy hash of the sample",
      "prediction": "Prediction of the sample"}
}
```

### Datasets

1. VX_Underground Dataset of 150GB compressed classified Malware
2. Scicore Dataset of compiled binaries (waiting on confirmation)
3. Public Datasets (Work in progress)


