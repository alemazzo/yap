from command import Command


class Update(Command):
    """
    Update a package.
    """

    def execute(self, packages: list, arguments: dict):
        raise NotImplementedError
