# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 20:50:41 2016

@author: sakbaria
"""

# https://polisen.se/Stockholms_lan/Aktuellt/Handelser/
#<a href="/Stockholms_lan/Aktuellt/Handelser/Stockholms-lan/2016-08-26-1126-Brand-Solna/">2016-08-26 11:26, Brand, Solna</a>

#https://polisen.se/Stockholms_lan/Aktuellt/RSS/Lokal-RSS---Handelser/Lokala-RSS-listor1/Handelser-RSS---Stockholms-lan/?feed=rss


import urllib.request
import re
import bs4

#pattern = '<title>(.+?) </title>'

#pattern2 = '<a href=(.+?)</a>'

#events =re.compile (pattern)

htmlfile = urllib.request.urlopen("https://polisen.se/Stockholms_lan/Aktuellt/RSS/Lokal-RSS---Handelser/Lokala-RSS-listor1/Handelser-RSS---Stockholms-lan/?feed=rss")

examplesoup = bs4.BeautifulSoup(htmlfile,"lxml") ## fungerar ej
#htmltext = htmlfile.read()

#event = events.findall(str(htmltext))


print (htmlfile)