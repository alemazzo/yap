import argparse


class Parser:
    def _get_real_parser(self):
        from yap.commands import get_commands

        parser = argparse.ArgumentParser(
            description='Yet Another Package-Manager')

        parser.add_argument('command',
                            choices=get_commands().keys(),
                            help='Command to execute')
        parser.add_argument('packages', help='Packages', nargs='*')
        return parser

    def parse(self):
        return self._get_real_parser().parse_args()


def parse_arguments():
    parser = Parser()
    args = parser.parse()
    return args
