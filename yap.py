import os
from github import Github, InputFileContent


token = open('.github_token', 'r').read().strip()
gh = Github(token)
user = gh.get_user()
user.create_gist(public=False, files={"yap.yml": InputFileContent(
    "my contents")}, description="Yap configuration")
