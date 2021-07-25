from command import Command


class Install(Command):
    """
    Install a package.
    """
    def execute(self, packages: list, arguments: dict):
        raise NotImplementedError
