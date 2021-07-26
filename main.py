#!/usr/bin/python3
from yap.arguments import parser
from yap.commands import get_command

if __name__ == '__main__':
    args = parser.parse_arguments()

    if not args.packages:
        parser.print_help()
        exit()
    
    command = get_command(args.command)
    packages = args.packages
    arguments = args

    command.execute(packages, arguments)
