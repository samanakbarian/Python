# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Authorise to let app access Twitter

import tweepy
from tweepy import OAuthHandler
 
consumer_key = 'j42eOiaAXmEOE3XyBcIGXA'
consumer_secret = 'Cj3AHLX5iXSghoUp5xHjdcG5dO5RQUSrf1T55ZXEno'
access_token = '913486483-ewQnsFsYyqkHwtoIB5qcU3OQm6zt2KbD90KXWVpN'
access_secret = 'RGJ6j1hTDWcJ9pLn7zr2FJw6bnSlMJg2aqMcF4nAA'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

###############################################

for status in tweepy.Cursor(api.home_timeline).items(10):
    print(status._json)

       
    # Process a single status
   # print(status.text) 
    
#for tweet in tweepy.Cursor(api.user_timeline).items():
#    print(tweet._json)
    
"""for friend in tweepy.Cursor(api.friends).items():
    print(friend._json)
    data= friend._json
    
    
print(data)"""

######################################################
## Streaming
#####################################################

