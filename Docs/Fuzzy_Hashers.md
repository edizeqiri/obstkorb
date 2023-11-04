# Fuzzy Hashers

## Machoc

The machoc hash is a fuzzy hash mechanism based on the _Call Flow Graph_ _(CFG)_ of a function.

### Algorithm

For each function, Machoc goes to every jump and takes note. Giving numbers for each block and fuzzy hashing them to produce a 32 bit output for each block.

Concatenate all the 32 bit hashes and you receive a machoc hash.

This is my idea of doing fuzzy hashing. The problem is that a lot of functions tend to come from libraries which might have an impact on the similarity. Need to analyze this further but have gotten to similiar results.

The maker promises, with empiric experiments that a 80% Jaccard distance indicates a good math between two binaries.

>Machoc hashes can also be used to diff two samples and rename automatically similar function. The function matching can be direct (same machoc hash), or based on heuristics. For example, given two functions in two binaries, if the surrounding functions in both binaries are direct matched, the two functions are probably similar despite producing a different hash.

## ssdeep

Good ol' ssdeep.

Originally from the piecewise hashing of Harbour Nicholas. Dcfldd. Defense Computer Forensics Lab. Available from: <http://dcfldd.sourceforge.net/>; 2002.
(Harbour, 2002)

Trigger points are used in place of fixed-sized blocks in **CTPH**. Whenever a particular trigger point is reached, the algorithm determines the hash value of the current data point. The trigger point criteria are selected such that when the amount of the input data increases, the final hash value does not rise irrationally. For instance, the trigger point for ssdeep depends on the amount of the input data because it requires 64 pieces per input file. The edit distance method is used by ssdeep to compare two files: The similarity between the files decreases with the number of steps required to convert one ssdeep hash value to another.[1]

[1] J. Kornblum, “Identifying almost identical files using context triggered piecewise hashing,” Digital Investigation, vol. 3, pp. 91–97, Sep. 2006, doi: 10.1016/j.diin.2006.06.015.

## TLSH - Trend Micro Locality Sensitive Hash

TLSH is a local sensitivity hash function. Meaning, it uses a sliding window to go over bytes and aggregates a header and body digest.
This gets done by using buckets and filtering data based on their quartile points. Quartile points are a measurent of the distribution of the bytes which get put into buckes.

The header conists mostly of the checksum of the byte string and the quartiles.
The body however consists of a statistial representation of the buckets. The algorithm checks for each index of the buckets in which quartile the bucket is in and encodes the result.

To measure the distance between two digests, TSLH uses an approximation of the hamming distance.[2]

[2] J. Oliver, C. Cheng, and Y. Chen, “TLSH -- A Locality Sensitive Hash,” in 2013 Fourth Cybercrime and Trustworthy Computing Workshop, Sydney NSW, Australia: IEEE, Nov. 2013, pp. 7–13. doi: 10.1109/CTC.2013.9.

# Conclusion

TLSH and ssdeep have the highest maturiy and will be the main comparison in my framework. Machoc has no literature and is therefore to be proven right.
