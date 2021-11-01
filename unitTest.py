import requests
import unittest
import config
import solved
import github
import issue
import run
class MyTest(unittest.TestCase):
    def setUp(self):
        self.beforeSolved = run.changeProblemsToList(issue.getIssue(config.GITHUB_REPO_URL, 1))
        self.nowSolved = solved.ProblemSettings().getSolved()

    def test_problemSetting(self):
        request = requests.get(solved.ProblemSettings().userSolvedUrl)
        self.assertEqual(request.status_code, 200)
    def test_getSolved(self):
        self.assertMultiLineEqual(f"{type(solved.ProblemSettings().getSolved())}","<class 'list'>")
    def test_getSolvedToday(self):
        if run.getSolvedToday(self.beforeSolved,self.nowSolved):
            return True
        else:
            return False
    def test_checkProblemsChanged(self):
        self.assertEqual(bool,type(run.checkProblemsChanged(self.beforeSolved,self.nowSolved)))
if __name__=="__main__":
    unittest.main()