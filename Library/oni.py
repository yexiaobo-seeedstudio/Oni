#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import argparse

from Oni import installer

def libraryInfo(name):
    pass

def libraryInstall(name):
    i = installer(name)
    i.install
    i.check
    i.finish

def executeCommand(command):
    if command.commands == 'install':
        # get the library file path
        for name in command.library:
            libraryInstall(name)

    if command.commands == 'info':
        for name in command.library:
            print command

def parseArgs():
    parser = argparse.ArgumentParser(description="Oni is an simple Arduino library manager.")
    parser.add_argument('commands',
                        action='store',
                        nargs='?',
                        help='command to manage Arduino libray')

    parser.add_argument('library',
                        action='store',
                        nargs='+',
                        help='name(s) of the library (e.g. "Grove_OLED96x64")')

    args = parser.parse_args()

    return args

def main():
    '''
    The entry for the program
    '''
    #TODO
    #x1. parse args
    # 2. implementing some commands: install remove info list search home
    # config
    #x2. get library's name

    args = parseArgs()
    executeCommand(args)

if __name__ == '__main__':
    main()
