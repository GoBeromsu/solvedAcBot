from github import Github
import config
import solved

g = Github(config.GITHUB_ACCESS_KEY)
print(g)
print(g.get_repo(config.GITHUB_REPO_URL))
print(g.get_repo(config.GITHUB_REPO_URL).get_issue(number=1))
def getIssue(repo_url,issue_num):
    issue = g.get_repo(repo_url).get_issue(number=issue_num)
    return issue.body

def updateIssue(repo_url,issue_num,content):
    issue = g.get_repo(repo_url).get_issue(number=issue_num)
    issue.edit(body=content)

def createIssue(repo_url,content):
    issue = g.get_repo(repo_url).create_issue(title='Solved Problems',body=content)

