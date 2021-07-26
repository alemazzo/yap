from .command import Command


class Install(Command):
    """
    Install a package.
    """
    def execute(self, packages: list=None, arguments: dict=None):
        raise NotImplementedError
