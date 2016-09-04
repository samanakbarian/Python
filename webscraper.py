# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 23:29:00 2016

@author: sakbaria

Project Web Scraping
"""

import urllib.request
import re
"""
#Tar ut enbart det som finns mellan taggarna
titleregex =re.compile ('<title>(.+?)</title>')  # Konverterar 
pattern = re.compile(regex) 
i=0
url = ["http://aftonbladet.se", "http://expressen.se","http://sydsvenskan.se", "http://blocket.se"]
while i <len(url):                                  # Loopar igenom url-listan
    htmlfile = urllib.request.urlopen(url[i])       # Öppnar url för varje element i url-listan
    htmltext = htmlfile.read()                      # Läser url
    titles = titleregex.findall(str(htmltext))      # Finner alla titlar på respektive websida baserat på titleregex definition
    
    print(titles)                                   # Printar ut titlarna
    
    i+=1
    
 """
###url = ["http://oppnajamforelser.socialstyrelsen.se/aldreguiden/Sidor/default.aspx?step=4&service=1&municipal=32&cities=32&performers=3005"]
   
html = urllib.request.urlopen("http://oppnajamforelser.socialstyrelsen.se/aldreguiden/Sidor/default.aspx?step=4&service=1&municipal=32&cities=32&performers=3005")

htmltext = html.read()

print(htmltext)





