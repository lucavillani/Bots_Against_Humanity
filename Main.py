import tweepy
from Credentials import consumer_key, consumer_secret, access_token, access_token_secret
import time
import random

# Function to combine random questions with rando answer
def create_tweet():
    global tweet

    questions = open("Cards_Against_Humanity_questions.txt").read()
    answers = open("Cards_Against_Humanity_answers.txt").read()

    question_list = questions.split("\n")
    answer_list = answers.split("\n")

    question = random.choice(question_list)
    if "?" in question:
        tweet = (question.replace("ANSW", random.choice(answer_list).strip(".")))
    else:
        tweet = (question.replace("ANSW", (random.choice(answer_list).lower()).strip(".")))

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Verify authentication
api.verify_credentials()
print("Authentication OK \n")

while True:
    create_tweet()

    # Text of the tweet
    print(tweet, "\n")

    # Tweet it
    api.update_status(tweet)

    # Time delay of 1h
    time.sleep(3600)


# Add other function inclduing automatic replies to users (create random answer function)
