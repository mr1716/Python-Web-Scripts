#!/usr/bin/env python
#Author: Mike R
#April 23rd, 2015

#Keeps track of news and prints when there is new news/post every minute.
#What this does is prints the time and any new net news from breakingnews.com, reddit.com/r/netsec, and other sites that update
#When user quits, will present all of the news and compiled info.

from bs4 import BeautifulSoup
import signal
import urllib
import time
import sys
global netSec
global breaking
global numStory
numStory=0
netSec=[]
breaking=[]

def getReddit(storyNum):
	localtime = time.asctime( time.localtime(time.time()) )
	if storyNum==0 :	
		print "\nReddit NetSec Post at :", localtime
		print "------------------------"
        html=urllib.urlopen('http://www.reddit.com/r/netsec/new')
        bt=html.read()

        soup=BeautifulSoup(bt)

        for link in soup.findAll('a', {'class': 'title may-blank '}):
#              	print link.extract() #prints everything selected
               	story=link.get_text()
               	if story not in netSec:
			if storyNum>0 :                       	
				print "\nReddit NetSec Post at :", localtime
				print "------------------------"
			netSec.append(story)
                       	print story

def getBreakingNews(storyNum):
	
	localtime = time.asctime( time.localtime(time.time()) )
        if storyNum==0 :
		print "\nBreaking News at :", localtime
        	print "------------------------"
	
	html=urllib.urlopen('http://www.breakingnews.com')
        bt=html.read()

        soup=BeautifulSoup(bt)
        for link in soup.findAll('div', {'class': 'headline'}):
                #print link.extract() prints everything selected
                story=link.get_text()
                if story not in breaking:
			if storyNum > 0:
				print "\nBreaking News at :", localtime
        			print "------------------------"			
			breaking.append(story)
                        print story

def ctrlc_handler(signum, frm):
	print 'Print the news from sources that occured while this was running'
	raise SystemExit

def ctrlz_handler(signum, frm):
	print 'Print the news from sources that occured while this was running'
	raise SystemExit

          
while True:
	signal.signal(signal.SIGINT, ctrlc_handler)
	signal.signal(signal.SIGTSTP, ctrlZ_handler)
	getReddit(numStory)
	getBreakingNews(numStory)	
	numStory+=1
	time.sleep(60)
