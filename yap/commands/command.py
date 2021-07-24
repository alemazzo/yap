class Command:

    def execute(self, packages: list, arguments: dict):
        raise NotImplementedError


def get_commands():
    from .install import Install
    from .uninstall import Uninstall
    from .search import Search
    from .update import Update

    COMMANDS = {
        'install': Install,
        'uninstall': Uninstall,
        'search': Search,
        'update': Update
    }

    return COMMANDS

def get_command(command: str):
    return get_commands()[command]()
