import tweepy
import os
import random

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

path = "/home/achmat/Random"
im = (path + "/" + random.choice(os.listdir(path)))
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
api.update_with_media(im,'Daily Dose of Laughter and Inspiration, All Random')