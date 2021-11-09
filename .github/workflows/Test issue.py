name: Test Issue
on:
  push:
    branches: [ master ]
jobs:
  run:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v1
    - name: Set up Python 3.9.x
      uses: actions/setup-python@v1
      with:
        python-version: 3.9.x
    - name: Install dependencies
      run: 
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Tweet
      env:
        GITHUB_ACCESS_KEY: ${{ secrets.GIT_ACCESS_KEY }}
        TWITTER_ACCESS_TOKEN_KEY: ${{ secrets.TWITTER_ACCESS_TOKEN_KEY }}
        TWITTER_ACCESS_TOKEN_SECRET: ${{ secrets.TWITTER_ACCESS_TOKEN_SECRET }}
        TWITTER_CONSUMER_KEY: ${{ secrets.TWITTER_API_KEY }}
        TWITTER_CONSUMER_SECRET: ${{ secrets.TWITTER_API_SECRET }}
      run: 
        python issue.py
