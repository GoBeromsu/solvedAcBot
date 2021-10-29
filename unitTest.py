import requests
import unittest

import solved

class MyTest(unittest.TestCase):
    def test_urlSettings(self):
        request = requests.get(solved.UrlSettings("310O").userSolvedUrl)
        self.assertEqual(request.status_code, 200)

if __name__=="__main__":
    unittest.main()