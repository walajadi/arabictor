#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2 juin 2015

@author: slim
'''
import urllib2

class Translator:
    def __init__ (self):
        pass
    
    def translate(self, text, source, target):
        """
            text : raw text to translate
            source : original text language
            target : translation output language
        """
        
    def normalize (self, text):
        pass

def translate(to_translate, to_langage="auto", langage="auto"):
    '''Return the translation using google translate
    you must shortcut the langage you define (French = fr, English = en, Spanish = es, etc...)
    if you don't define anything it will detect it or use english by default
    Example:
    print(translate("salut tu vas bien?", "en"))
    hello you alright?'''
    agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
    before_trans = 'class="t0">'
    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_langage, langage, to_translate.replace(" ", "+"))
    request = urllib2.Request(link, headers=agents)
    page = urllib2.urlopen(request).read()
    result = page[page.find(before_trans)+len(before_trans):]
    result = result.split("<")[0]
    return result

if __name__ == '__main__':
    to_translate = 'Io mangio il cibo'
    print("%s >> %s" % (to_translate, translate(to_translate)))
    print("%s >> %s" % (to_translate, translate(to_translate, 'fr')))
    #should print Hola como estas >> Hello how are you
    #and Hola como estas? >> Bonjour comment allez-vous?