#!/usr/bin/env python

#Run DIG command to get full data from website
#Author: Mike R
#Date: 12/9/2015

import subprocess

#Ask user for site
site=raw_input("Target site:")

#dig command
#get all information
p = subprocess.Popen(['dig', site, ANY], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print out #maybe worth printing to a file?
