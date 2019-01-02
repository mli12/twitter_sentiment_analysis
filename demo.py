#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 16:28:27 2019

@author: sendofuji
"""

from textblob import TextBlob
import tweepy
import csv

consumer_key = 's1K8ElhDZSTZm76ZHnOBDMJU4'
consumer_secret = 'E2U9PedbLiCnZFOHY1nWEb72lSycXrmpIP54tznco9WFpP4ch4'

access_token = '443426356-Ypk82XOaBvo7JU7Wi8ZzePdZ0TX4sGDxqjpJWXII' 
access_token_secret = '2q2pp3wtfVmWyGUZadOQvOl04hoyGv9TGnGEoO3CEvtAc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search('Trump')

def get_label(polarity, threshold = 0):
        if polarity > threshold:
            return 'positive'
        elif polarity == threshold:
            return 'neutral'
        else:
            return 'negative'


with open ('sentiment_assignment.csv','w') as f:
    fieldnames = ['tweet','polarity']
    writer = csv.DictWriter(f, fieldnames = fieldnames)

    writer.writeheader()
    
    for tweet in public_tweets:
        
        polarity = TextBlob(tweet.text).sentiment.polarity
        label = get_label(polarity)
        writer.writerow({'tweet': tweet.text, 'polarity': label})