from .manager import Manager

class Apt(Manager):

    """
    The APT package manager interface.
    """

    def __init__(self):
        super().__init__()