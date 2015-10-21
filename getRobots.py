#!/usr/bin/env python
#Author: Mike R
#Written September 2015
#What it does it combs through the top 1000 websites robots.txt and then finds the most common allowed directories. Prints top 10 allowed.

import urllib2, re
from collections import Counter
import collections
robotDirs = []

#Insert list of websites into top-1m.csv. Alternatively, user could input some sites manually
sites=open('top-1m.csv', 'r')

#loop for all 1k sites!
for line in sites:
	line=line.rstrip()
	print line
	line='http://www.' + line

	# add /robots.txt
	newSite=line + '/robots.txt'
	try:
		data=urllib2.urlopen(newSite).read()
		lines=data.splitlines(True)

		for data2 in lines:
			if "Allow:" in data2: 
				if(re.match("Allow:","Allow:")):
					robotDirs.append(data2[7:] ) #if unique, then add to the list. Otherwise, add 1
	except:
		print "Doesn't work"
#Once complete, make sure to count number of times they exist
counter=collections.Counter(robotDirs)
print counter.most_common(10)
