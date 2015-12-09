#!/usr/bin/env python

#Run host command to provide host command data from user desired website
#Author: Mike R
#Date: 12/9/2015

import subprocess

#Ask user for site
site=raw_input("Target site:")

#Host command
#get all of the host information for the site
p = subprocess.Popen(['host', '-a', site], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print out #maybe worth printing to a file?

#Host command
#get verbose response
p = subprocess.Popen(['host', '-d', site], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate()
print out #maybe worth printing to a file?
