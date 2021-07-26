from .command import Command
from yap.gh.auth import TokenManager
from github import Github

class Start(Command):
    """
    Search a package.
    """

    def execute(self, packages: list=None, arguments: dict=None):
        tkManager = TokenManager()
        token = tkManager.get_token()

        gh = Github(token)
        user = gh.get_user()

        print(user)

