from requests import get, post
import json
import os, os.path
from github import Github, InputFileContent 


class TokenManager():

    """
    GitHub Access Token manager.
    If the request token is not present, it will be requested, otherwise it will be used.
    The token is stored in the dot folder.
    """

    _DOT_FOLDER = '.yap'
    _TOKEN_FILE = '.token'

    _SCOPE = 'gist'
    _GRANT_TYPE = 'urn:ietf:params:oauth:grant-type:device_code'

    _DEVICE_LINK = 'https://github.com/login/device/code'
    _ACTIVATE_LINK = 'https://github.com/login/device'
    _TOKEN_LINK = 'https://github.com/login/oauth/access_token'


    def __init__(self):
        self._client_id = open('.client_id').read()

    def _create_dot_folder(self):
        folder = os.path.join(os.path.expanduser('~'), TokenManager._DOT_FOLDER)
        if not os.path.isdir(folder):
            os.mkdir(folder)

    def _save_token(self, token):
        self._create_dot_folder()
        path = os.path.join(TokenManager._DOT_FOLDER, TokenManager._TOKEN_FILE)
        open(path, 'w').write(token)

    def _get_new_token(self):
        """
        Get new token with Device-Flow procedure.
        More info at https://docs.github.com/en/developers/apps/building-oauth-apps/authorizing-oauth-apps#device-flow
        """
        def to_dict(string: str):
            # Github response to dictionary
            args = {}
            for var in string.split('&'):
                key, value = var.split('=')
                args[key] = value
            return args
        
        # Get user and device code
        res = post(TokenManager._DEVICE_LINK, data={
            'client_id': self._client_id,
            'scope': TokenManager._SCOPE
        })
        response = to_dict(res.text)
        user_code = response['user_code']
        device_code = response['device_code']

        # Ask the user to grant access to the application
        print(f'Go to {TokenManager._ACTIVATE_LINK} and enter the following code: {user_code}')
        input('Press enter when you had grant the access...')
        
        # Get the access token of the user
        res = post(TokenManager._TOKEN_LINK, data={
            'client_id': self._client_id,
            'device_code': device_code,
            'grant_type': TokenManager._GRANT_TYPE
        })
        response = to_dict(res.text)
        token = response['access_token']


        self._save_token(token)
        return token

    def get_token(self):
        token_path = os.path.join(TokenManager._DOT_FOLDER, TokenManager._TOKEN_FILE)
        token_path = os.path.join(os.path.expanduser('~'), token_path)
        if os.path.isfile(token_path):
            return open(token_path).read()
        else:
            return self._get_new_token()

