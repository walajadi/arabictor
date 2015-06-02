#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 2 juin 2015

@author: slim
'''
import urllib2


print 'hello world'
the_url = 'http://www.voidspace.org.uk'
req = urllib2.Request(the_url)
handle = urllib2.urlopen(req)
the_page = handle.read()
print the_page