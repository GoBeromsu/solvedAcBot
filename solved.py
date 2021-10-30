import requests

class UrlSettings(object):
    def __init__(self, userName):
        self.api_server = "https://solved.ac/api"
        self.userName = userName
        self.userSolvedUrl = (
            self.api_server + "/v3/search/problem?query=solved_by:" + self.userName
        )

## 푼 문제 정보를 string으로 가공하는 메소드


def getSolved():
    problems = []
    url = UrlSettings("310o").userSolvedUrl
    data = requests.get(url).json()

    for problem in data["items"]:
        id = problem["problemId"]
        title = problem["titleKo"]
        problems.append([id,title])
    return problems
