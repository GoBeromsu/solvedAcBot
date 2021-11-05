import issue
import tweet
import config
import solved
import github
def getSolvedToday(bSolved,nSolved):
    stack = []
    for problem in nSolved:
        if problem not in bSolved:
            stack.append(problem)
    return stack
def changeProblemsToList(body:str):
    problems = []
    for problem in body.split('\n'):
        if problem != '':                
            idx = problem.find(' ')
            number = int(problem[:idx])
            title = problem[idx+1::]
            problems.append([number,title])

    return problems
def changeProblemsToStr(problems:list):
    body =""
    for problem in problems:
        number = problem[0]
        title = problem[1]
        body+=f"{number} {title}\n"
    return body
def updateProblems(nowSolved):
    issue.updateIssue(config.GITHUB_REPO_URL,1,changeProblemsToStr(nowSolved))
def checkProblemsChanged(beforeSolved:list,nowSolved:list):
    return True if len(beforeSolved) != len(nowSolved) else False
def formatTweet(solvedToday:list):
    tweet = 'Today I Solved \n'
    tweet += formatProblems(solvedToday)
    tweet+='#solvdac \n'
    tweet+=f'solved.ac/profile/{config.GITHUB_ID}'
    return tweet
def formatProblems(solvedToday:list):
    tweet=''
    count=1
    for problem in solvedToday:
        if count ==4:
            tweet+= f"「{problem[0]} {problem[1]}」...\n"
            break
        tweet+= f"「 {problem[0]} {problem[1]} 」\n"
        count+=1
    return tweet

def main():
    nowSolved = solved.ProblemSettings().getSolved()
    try: 
        beforeSolved = changeProblemsToList(issue.getIssue(config.GITHUB_REPO_URL, 1))
    except github.GithubException:
        print("Github Exception Error occured")
        issue.createIssue(config.GITHUB_REPO_URL, changeProblemsToStr(nowSolved))
        print("Create init Issue")
    if checkProblemsChanged(beforeSolved, nowSolved):
        solvedToday = getSolvedToday(beforeSolved, nowSolved)
        updateProblems(nowSolved)
        body = formatTweet(solvedToday)
        tweet.post(body)
    else:
        print("오늘 안 풀었구먼")
        print("Is it working?")

if __name__=="__main__":
    main()

