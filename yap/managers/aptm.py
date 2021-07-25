from manager import Manager
import apt

class Apt(Manager):

    """
    The APT package manager interface.
    """

    def __init__(self):
        super().__init__()
        self.cache = apt.cache.Cache()
        self.cache.update()
        self.cache.open()


    def install(self, package):
        """
        Install a package.
        """
        self.cache.get(package).mark_install()
        self.cache.commit()
