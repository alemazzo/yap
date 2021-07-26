from .command import Command


class Uninstall(Command):
    """
    Uninstall a package.
    """
    def execute(self, packages: list=None, arguments: dict=None):
        raise NotImplementedError
