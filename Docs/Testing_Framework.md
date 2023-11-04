# Testing Framework

This document will display how the testing should be done. Work in progress, therefore changes can occur.

## Concept

1. Sample 5 times from 1-5 of each family
2. Create a hash for each sample
3. Save them into mongoDB
4. Go through all of the data and hash with all the hashers
5. Save the results into mongoDB

## Database Schema

I will create 4 collections in MongoDB:
The schema for each hasher:

```json
{
    "family": "Name of the family",
    "SHA256": "SHA256 of the sample",
    "fuzzy_hash": "Fuzzy hash of the sample",
    "prediction": "Predicted family of the sample"
}
```

### Datasets

1. VX_Underground Dataset of 150GB compressed classified Malware
2. Scicore Dataset of compiled binaries (waiting on confirmation)
3. Public Datasets


