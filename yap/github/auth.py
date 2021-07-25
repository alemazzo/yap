from requests import get, post
import json
from github import Github, InputFileContent
import os, os.path

hd = os.path.expanduser('~')
yap_folder = os.path.join(hd, '.yap')

def toDict(response: str):
    args = {}
    for var in response.split('&'):
        key, value = var.split('=')
        args[key] = value
    return args

# Check if file exists
def isFile(path: str):
    return os.path.isfile(path)

def login():
    client_id = open('.client_id').read()
    res = post('https://github.com/login/device/code', data={
        'client_id': client_id,
        'scope': 'gist'
        })

    args = toDict(res.text)
    print(args['user_code'])

    input('Press enter to continue...')
    res = post('https://github.com/login/oauth/access_token', data={
        'client_id': client_id,
        'device_code': args['device_code'],
        'grant_type': 'urn:ietf:params:oauth:grant-type:device_code'
    })

    args = toDict(res.text)
    token = args['access_token']
    print(token)

    # Create an hidden folder in home directory in this pc
    os.mkdir(yap_folder)
    open(os.path.join(yap_folder, '.token'), 'w').write(token)

    return token


if isFile(os.path.join(yap_folder, '.token')):
    token = open(os.path.join(yap_folder, '.token')).read()
else:
    token = login()

gh = Github(token)
user = gh.get_user()

gist = None
for gs in user.get_gists():
    if 'yap.yml' in gs.files.keys():
        gist = gs

file = gist.files['yap.yml']
gist.edit(files = {'yap.yml' : InputFileContent(file.content + " --- ")})




"""
user = gh.get_user()
user.create_gist(public=False, files={"yap-config2.yml": InputFileContent(
    "#Yap Configuration")}, description="Yap configuration")
"""
