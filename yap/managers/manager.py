
class Manager():
    """
    A package-manager interface.
    """

    def search(self, package: str, arguments: dict):
        raise NotImplementedError

    def install(self, package: str, arguments: dict):
        raise NotImplementedError

    def uninstall(self, package: str, arguments: dict):
        raise NotImplementedError

    def update(self, package: str, arguments: dict):
        raise NotImplementedError

    
    def __str__(self):
        return self.__class__.__name__