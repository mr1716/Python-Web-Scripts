#!/usr/bin/env python

#This program gets news from BreakingNews.com
#Written By Mike R
#April 13th-14th, 2015

#What this does is prints the time and any new net news from breakingnews.com
from bs4 import BeautifulSoup
import urllib
import time

localtime = time.asctime( time.localtime(time.time()) )
print "Breaking News at :", localtime
print "------------------------\n\n"
stories=[]
while True:
	html=urllib.urlopen('http://www.breakingnews.com')
	bt=html.read()
	
	soup=BeautifulSoup(bt)

	for link in soup.findAll('div', {'class': 'headline'}):		
 		#print link.extract() prints everything selected
		story=link.get_text()
		if story not in stories:
			localtime = time.asctime( time.localtime(time.time()) )
			print "\n\nBreaking News at :", localtime
			print "------------------------\n"
			stories.append(story)
			print story + "\n\n"
	
	time.sleep(60)
