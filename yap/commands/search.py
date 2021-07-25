from command import Command


class Search(Command):
    """
    Search a package.
    """

    def execute(self, packages: list, arguments: dict):
        raise NotImplementedError
