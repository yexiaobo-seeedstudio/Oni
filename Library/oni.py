#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys

def executeCommand( args ):
    pass

def usage():
    u = """\
Intro:
    Oni is an simple Arduino library manager.

Usage:
    oni command [options] library ...

command:
    info    : information of the library
    install : install library
    remove  : remove library
    list    : list all library which have been installed
    search  : search what you want
    home    : open the library homepage
    config  : listing all Oni setup information

example:
    oni install Grove_Relay
    """
    return u

def parseArgs():
    pass

def main():
    '''
    The entry for the program
    '''
    #TODO
    # 1. parse args
    # 2. implementing some commands: install remove info list search home
    # config
    # 2. get library's name

    if len(sys.argv) < 2:
        print usage()

    args = parseArgs()
    executeCommand(args)

if __name__ == '__main__':
    main()
