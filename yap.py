#!/usr/bin/python3
from yap import parser

if __name__ == '__main__':
    args = parser.parse_arguments()
    
    command = args.command
    packages = args.packages

    print(f'command = {args.command}')
    print(f'packages = {args.packages}')
