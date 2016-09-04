# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 21:17:12 2016

@author: sakbaria
"""

# $price.0">106.02</span>

#https://finance.yahoo.com/quote/AAPL/?p=AAPL

import urllib.request
import re

pattern = '$price.0"(.+?)</span>'
priceregex =re.compile (pattern)

htmlfile = urllib.request.urlopen("https://finance.yahoo.com/quote/AAPL/?p=AAPL")

htmltext = htmlfile.read()

price = priceregex.findall(str(htmltext))


print (price)
