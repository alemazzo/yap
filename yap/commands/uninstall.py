from command import Command


class Uninstall(Command):
    """
    Uninstall a package.
    """
    def execute(self, packages: list, arguments: dict):
        raise NotImplementedError
