import pyimpfuzzy
from icecream import ic
hash1 = pyimpfuzzy.get_impfuzzy("../Testing_Framework/Samples/0f9e27ec1ed021fd7375ca46f233c06b354d12d57aed44132208cd9308bfee11")
hash2 = pyimpfuzzy.get_impfuzzy("../Testing_Framework/Samples/0414ffdf9dcf32061cc57d0b54bf4410c1c588258c12615988e3ce8cb0cf4fb4")


ic(pyimpfuzzy.hash_compare(hash1,hash2))