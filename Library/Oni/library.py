#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Library():
    ''' Basic Library module '''
    def __init__(self):
        name     = ""
        url      = ""
        homepage = ""
        isGit    = False
        isHg     = False
        isSvn    = False
        isZip    = False
        cmd      = ""

    def install(cmd):
        os.system(cmd)

    def CMD():
        if isGit:
            cmd = "git clone "

        if isHG:
            cmd = "hg clone "

        if isSvn:
            cmd = "svn co "

        if isZip:
            #FIXME
            cmd = "curl -O"
