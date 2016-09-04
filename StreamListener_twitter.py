# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 23:38:24 2016

@author: sakbaria
"""

## Class StreamListener 
## Listen to a specific hash tag

from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):
    
    def on_data(self,data):
        try:
            with open('python.json','a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print(str(e))
        return True
            
                