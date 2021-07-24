#!/usr/bin/python3
from yap.arguments import parser
from yap.commands import get_command

if __name__ == '__main__':
    args = parser.parse_arguments()
    
    cmd = args.command
    packages = args.packages
    arguments = args

    command = get_command(cmd)
    print(f'command = {command}')
    print(f'packages = {packages}')
    print(f'arguments = {arguments}')
