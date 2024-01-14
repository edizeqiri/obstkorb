import unittest
import os
from TLSH import TLSH
from icecream import ic
class MyTestCase(unittest.TestCase):

    def test_tlsh(self):
        path = "Samples/006c74c6813a6efeabea860b2718ed548eed216a319d76ceb178fc38cba458d1.exe"
        with open(path, "rb") as file_handler:
            file = {
                "data": file_handler.read(),
                "path": path
            }

        self.assertEqual(ic(TLSH.hash(file)), "T18A635B27E9548473CDC24DB044E80B7B8A77B6B007656CA7EF48D6551EB01F4BA3E22B")
        self.assertEqual(TLSH.predict(path, "malware"), "LgoogLoader")


if __name__ == '__main__':
    unittest.main()
