#!/usr/env/python
from bs4 import BeautifulSoup
import urllib

#Mike R
#BeautifulSoup example

html=urllib.urlopen("http://espn.go.com")
print html

bt=BeautifulSoup(html.read(), "lxml") #read, parser wanted. By default uses HTML which is not the best available.

print(bt) #give output on entire output of the document
#print title of document. BS has tag options
print(bt.title) #In HTML, there is only 1 title. SO this is it.
print(bt.title.string)
#navigable string. Getting the actual string inside
#default Beautiful Soup returns unicode strings!!!
print bt.title.name #exact tag
#get meta tag
print bt.meta
#print next meta tag
print bt.meta.next
print bt.meta.next.next
#find method to search for tag
#find for singular return. return all matches find_all
allMetaTags = bt.find_all('meta')
print allMetaTags
#returns list of all meta tags
#first element of list
print allMetaTags[0]
#access as dictionary values
print allMetaTags[0]['content']
#print allMetaTags[0]['http-equiv']
#find_all take in regular expression. CSS selector searching and other functions
allMetaTags=bt.find_all('meta')
#find links in current HTML file
allLinks = bt.find_all('a')
#a tags and print href values
print len(allLinks)
for link in allLinks:
	print link['href']
#print relative and full links.
bt.get_text()
