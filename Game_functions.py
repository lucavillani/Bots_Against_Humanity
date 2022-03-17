import random

global tweet

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
        tweet = (question.replace("ANSW", random.choice(answer_list).lower().strip(".")))

create_tweet()