from github import Github, InputFileContent
from auth import TokenManager

tkmanager = TokenManager()
token = tkmanager.get_token()

gh = Github(token)
user = gh.get_user()

repo = user.get_repo('yap')
print(repo)

"""
gist = None
for gs in user.get_gists():
    if 'yap.yml' in gs.files.keys():
        gist = gs

file = gist.files['yap.yml']
gist.edit(files = {'yap.yml' : InputFileContent(file.content + " --- ")})
"""



"""
user = gh.get_user()
user.create_gist(public=False, files={"yap-config2.yml": InputFileContent(
    "#Yap Configuration")}, description="Yap configuration")
"""
