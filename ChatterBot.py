# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "ec6gL3ASXa7jBNNmb3tuyVsJM"
consumer_secret = "bOtaxqvBur8bVxiSLf6qkFXr1QXqmQZGP664c3iIOOB8EweWSk"
access_token = "969399323145289729-E6sNmYKi96fMPFBKs7BmynG9VQ2LoN4"
access_token_secret = "4YsEHlScIp9YNb0IrEkvT7fJemTGYjnnPgoVW8fpJF4g9"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE
