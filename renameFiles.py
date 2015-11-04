#!/usr/bin/env python
#Author: Mike R

#Will allow users to change extension of file

import os
import shutil

#files can be changed.
name=raw_input("Which file to look for (name and extension):")
path="/"


result = []
for root, dirs, files in os.walk(path):
    if name in files:
        result.append(os.path.join(root, name))
        #rename the file with new extension that can be changed.
        newName=os.path.splitext(name)[0]+'.zip'
        print newName
        os.system("mv " + name + " " + newName)
