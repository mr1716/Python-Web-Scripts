#!/usr/bin/env python
#Author: Mike R
#Date: Thursday, October 8th, 2015

#Code that prints all forms and the form fields in each in a given website.
import mechanize

#getting the website
website=raw_input("Please input a website to crawl the forms:")

br=mechanize.Browser()

#fetching the website
br.open(website)


#dump all the forms
for form in br.forms():
	print form
