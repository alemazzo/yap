class Command:

    def execute(self, packages: list=None, arguments: dict=None):
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


def get_commands():
    from .install import Install
    from .uninstall import Uninstall
    from .search import Search
    from .update import Update
    from .start import Start

    COMMANDS = {
        'start': Start,
        'install': Install,
        'uninstall': Uninstall,
        'search': Search,
        'update': Update
    }

    return COMMANDS

def get_command(command: str):
    return get_commands()[command]()
