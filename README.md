# solved.ac Bot

solved.ac API를 사용하여 오늘 푼 문제를 가져와서 Github 이슈에 저장하고, 
어제 푼 문제와 비교하여 추가 된 문제를 트윗합니다. 
또한, Github 액션을 통해 자동화되며, 이슈를 데이터베이스처럼 사용하고 cron으로 실행됩니다.

- solved.ProblemSettings().getSolved()를 통해 오늘 푼 문제를 가져옵니다.
- issue.getIssue(config.GITHUB_REPO_URL, 1)를 통해 이전에 저장된 문제를 가져옵니다.
- checkProblemsChanged(beforeSolved, nowSolved)를 통해 오늘 추가 된 문제가 있는지 확인합니다.
- 문제가 추가된 경우, getSolvedToday(bSolved,nSolved)를 통해 추가 된 문제를 가져옵니다.
- updateProblems(nowSolved)를 통해 현재 푼 문제를 이슈에 업데이트합니다.
- formatTweet(solvedToday)를 통해 트윗할 메시지를 포맷팅합니다.
- tweet.post(body)를 통해 메시지를 트윗합니다.
- Github 액션을 통해 이전에 저장된 문제를 가져오고, 자동으로 실행됩니다.
- 이슈를 데이터베이스처럼 사용하여 현재 푼 문제를 저장하고, cron으로 실행됩니다.

### 모듈

- issue: 깃허브 이슈를 다루는 모듈
- tweet: 트위터 API를 다루는 모듈
- config: 설정값을 담고 있는 모듈
- solved: solved.ac API를 이용하여 사용자가 푼 문제를 가져오는 모듈

### 기능 명세

- getSolvedToday(): 이전에 푼 문제와 오늘 푼 문제를 비교하여 새로 푼 문제를 찾아냅니다.
- changeProblemsToList(): 깃허브 이슈의 내용을 파싱하여 이전에 푼 문제 목록을 리스트 형태로 반환합니다.
- changeProblemsToStr(): 문제 목록을 깃허브 이슈의 내용 형식으로 변환하여 반환합니다.
- updateProblems(): 깃허브 이슈를 업데이트합니다.
- checkProblemsChanged(): 이전에 푼 문제와 오늘 푼 문제를 비교하여 새로 푼 문제가 있는지 확인합니다.
- formatTweet(): 트위터에 게시할 텍스트를 포맷팅합니다.
- formatProblems(): 트위터에 게시할 문제 목록을 포맷팅합니다.

위 함수들을 이용하여 사용자가 푼 문제를 트위터에 게시하는 역할을 합니다.## 참조

[twitter-lyric-bot](https://github.com/ryanking13/twitter-lyric-bot)
