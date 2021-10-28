import requests
from unittest import TestCase


class MyTest(TestCase):
    def test_urlSettings(self):
        request = requests.get(UrlSettings("310o").userSolvedUrl)
        self.assertEqual(request.status_code, 200)


class UrlSettings(object):
    def __init__(self, userName):
        self.api_server = "https://solved.ac/api"
        self.userName = userName
        self.userSolvedUrl = (
            self.api_server + "/v3/search/problem?query=solved_by:" + self.userName
        )

## 푼 문제 정보를 string으로 가공하는 메소드


def getSolved():
    problems = {}
    url = UrlSettings("310o").userSolvedUrl
    data = requests.get(url).json()

    for problem in data["items"]:
        id = problem["problemId"]
        title = problem["titleKo"]
        problems[id]=title
    return problems
print(getSolved())