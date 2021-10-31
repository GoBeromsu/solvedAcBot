import requests
import unittest
import config
import solved
import github
class MyTest(unittest.TestCase):
    def test_problemSetting(self):
        request = requests.get(solved.ProblemSettings().userSolvedUrl)
        self.assertEqual(request.status_code, 200)
    def test_getSolved(self):
        self.assertMultiLineEqual(f"{type(solved.ProblemSettings().getSolved())}","<class 'list'>")
    def test_updateProblems(self):
        return True
    def test_checkProblems(self):
        return True
    
if __name__=="__main__":
    unittest.main()