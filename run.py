import issue
import config
import solved
# 오늘까지 푼 문제와 어제까지 푼 문제를 비교
# 비교 후 같으면 트윗 X, 다르면 트윗
# 두 입력 값의 길이를 비교함
# 길이가 다른 경우 첫 인덱스부터 비교해가며 다른 값이 나올 경우 스택에 넣고
# 다시 그 자리에서 다시 시작함

def updateProblems():
    pass

def checkProblems(bProblems:list,nProblems:list):
    return True if len(bProblems) == len(nProblems) else False
    
def formatProblems(body:str):
    problems = []
    for problem in body.split('\n'):
        idx = problem.find(' ')
        number = problem[:idx]
        title = problem[idx+1::]
        problems.append([number,title])
    problems.pop()
    return problems
    

def main():
    beforeSolvedProblems = formatProblems(issue.getIssue(config.GITHUB_REPO_URL, 1))
    nowSolvedProblems = solved.getSolved()
    print(len(beforeSolvedProblems))
    print(len(nowSolvedProblems))
    if not checkProblems(beforeSolvedProblems, nowSolvedProblems):
        pass
    else:
        pass

if __name__=="__main__":
    main()