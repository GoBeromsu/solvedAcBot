import requests
import config
class ProblemSettings(object):
    def __init__(self):
        self.api_server = "https://solved.ac/api"
        self.userName = config.GITHUB_ID
        self.userSolvedUrl = (
            self.api_server + "/v3/search/problem?query=solved_by:" + self.userName
        )
    def getSolved(self):
        problems = []
        page=1
        while 1:
            data = requests.get(self.userSolvedUrl+f"&page={page}").json()
            for problem in data["items"]:
                id = problem["problemId"]
                title = problem["titleKo"]
                problems.append([id,title])
            if not data['items']:
                break
            else:
                page+=1
        return problems