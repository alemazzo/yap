#!/usr/bin/python3
from yap.arguments import parser
from yap.commands import get_command

if __name__ == '__main__':
    args = parser.parse_arguments()
    
    command = get_command(args.command)
    packages = args.packages
    arguments = args

    print(f'command = {command}')
    print(f'packages = {packages}')
    print(f'arguments = {arguments}')
