import tweepy
from Credentials import consumer_key, consumer_secret, access_token, access_token_secret
from Game_functions import tweet

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Verify authentication
api.verify_credentials()
print("Authentication OK \n")

# Text of the tweet
print(tweet)

# Tweet
api.update_status(tweet)

#https://realpython.com/twitter-bot-python-tweepy/
# Add other function inclduing automatic replies to users (create random answer function)