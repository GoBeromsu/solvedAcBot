import issue

import config
import solved

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


def main():

    beforeSolved = changeProblemsToList(issue.getIssue(config.GITHUB_REPO_URL, 1))
    nowSolved = solved.ProblemSettings().getSolved()

    if checkProblemsChanged(beforeSolved, nowSolved):
        solvedToday = getSolvedToday(beforeSolved, nowSolved)
        updateProblems(nowSolved)
        print(solvedToday)
    else:
        print("오늘 안 풀었구먼")



if __name__=="__main__":
    main()
