import sys
import requests

# 2021F CPE 551-WS Final Project
#   a script to look up all the github repositories belonging to a user and star them

# usage
#   python main.py {github_token} {github_username}

github_token = sys.argv[1]
github_username = sys.argv[2]

session = requests.Session()
session.headers = {'Authorization': 'token %s' % github_token }

repos_endpoint = 'https://api.github.com/users/%s/repos' % github_username
repos = session.get(repos_endpoint).json()

for repo in repos:
  print 'starring: %s' % repo['url']
  star_endpoint = 'https://api.github.com/user/starred/%s/%s' % (github_username, repo['name'])
  session.put(star_endpoint)