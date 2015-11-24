# -*- coding: utf-8 -*-

import tweepy
import json
import time
import sys
import re
from progressbar import ProgressBar, Percentage
from tweepy.streaming import StreamListener
from tweepy import Stream, OAuthHandler


consumer_key = 'eYtlRfpCcqhKPUvHryQFjQK3j'
consumer_secret = 'nA9u4Dc18etdLnVCMG392lrkQvSZvqJPMTgxqUXHA8u0XTibNC'
access_token = '2748894438-YRYwvD9pjeZhhn5OvVcuChKke3DSDC2WVqPdAkG'
access_token_secret = 'BNtBO0TUjTf39PT9XbLsM1FCUCjejw52IZ2aKtbHtFXNG'


    

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
max_tweet=input('amount tweets: ')

    
api = tweepy.API(auth,retry_count=3, retry_delay=5,retry_errors=set([401, 404, 420, 500, 503]))

class sonListener(tweepy.StreamListener):
    def __init__(self, api=None):
        self.num_tweet = 0
        self.pbar = ProgressBar(widgets=[Percentage()], maxval=max_tweet).start()
    def on_data(self, data):
        decoded = json.loads(data)
        with open ('twitt.txt','a') as workfile:
                
            print '\n Text: %s  \n' % (decoded['text'].encode('ascii', 'ignore'))        

            workfile.write('Language: %s  \n' % (decoded['lang'].encode('ascii', 'ignore')))
            self.num_tweet += 1
            if self.num_tweet >= max_tweet:
                self.pbar.finish()
                
                lang1=raw_input('language:')
                lang2=raw_input('language:')
                lang3=raw_input('language:')
                workfile = open("twitt.txt", 'r')
                leng1 = leng2 = leng3 = 0
                
                for s in workfile :
                    i = s.find('%s' %(lang1))
                    if i > -1:
                            leng1 += 1
                    else:
                        i = s.find('%s' %(lang2))
                        if i > -1:
                                leng2 += 1
                        else:
                            i = s.find('%s' %(lang3))
                            if i > -1:
                                    leng3 += 1
                
                print( '%s twitts '% (max_tweet))
                print('%s was used %s times'% (lang1,leng1))
                print('%s was used %s times'% (lang2,leng2))
                print('%s was used %s times'% (lang3,leng3))
                sys.exit(0)
            
                

            else:
                self.pbar.update(self.num_tweet)
            return True

        
tweet=raw_input('tweets: ')        
s = sonListener()

stream = tweepy.Stream(auth, s)
stream.filter(track=['%s'%(tweet)])









   
    
