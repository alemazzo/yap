from .command import Command


class Search(Command):
    """
    Search a package.
    """

    def execute(self, packages: list=None, arguments: dict=None):
        raise NotImplementedError
