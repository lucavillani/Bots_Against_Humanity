import tweepy
from Credentials import consumer_key, consumer_secret, access_token, access_token_secret
import time
import random

# Login and open the API
def authentication():
    global api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

# Verify authentication
def verify_authentication():
    api.verify_credentials()
    print("Authentication OK \n")

# Open and read the txt file with list of questions and answers
def read_text():
    global question_list, answer_list
    questions = open("Cards_Against_Humanity_questions.txt").read()
    answers = open("Cards_Against_Humanity_answers.txt").read()

    question_list = questions.split("\n")
    answer_list = answers.split("\n")

# Function to combine random questions with rando answer
def create_tweet():
    global tweet
    question = random.choice(question_list)
    if "?" in question:
        tweet = (question.replace("ANSW", random.choice(answer_list).strip(".")))
    else:
        tweet = (question.replace("ANSW", (random.choice(answer_list).lower()).strip(".")))

# Send the tweet to the Twitter bot
def send_tweet_to_bot():
    api.update_status(tweet)

# Run all the previous functios
def main():
    authentication()
    verify_authentication()
    read_text()
    create_tweet()
    send_tweet_to_bot()

while True:
    main()

    # Text of the tweet
    print(tweet, "\n")

    # Time delay of 1h
    time.sleep(3600)

# Add other function inclduing automatic replies to users (create random answer function)
