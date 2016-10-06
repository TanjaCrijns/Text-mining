import numpy as np
import pandas, re, sklearn

if __name__ == "__main__":
    with open("D:/Users/Tanja/Documents/Master/Text-Mining/Assignment5/files/negative_words.txt", "r") as f:
        negwords = [word[:-1] for word in f.readlines()]
        f.close()
    with open("D:/Users/Tanja/Documents/Master/Text-Mining/Assignment5/files/positive_words.txt", "r") as f:
        poswords = [word[:-1] for word in f.readlines()]
        f.close()
    df = pandas.read_excel("D:/Users/Tanja/Documents/Master/Text-Mining/Assignment5/files/tweets.xlsx")
    tweets = df.ix[:,'Tweet'].values.tolist()
    labels = df.ix[:,'Manual Annotation'].values.tolist()
    neutral = 0
    positive = 0
    negative = 0
    for label in labels:
        if label == 0:
            neutral += 1
        elif label == 1:
            positive += 1
        else:
            negative += 1
    print "Neutral = {}\nPositive = {}\nNegative = {}".format(neutral, positive, negative)

    tweets = [tweet.lower() for tweet in tweets]
    tweets = [re.sub (r'[^\w\s#@]', "", tweet) for tweet in tweets]
    for index in range(len(tweets)):
        for word in tweets[index].split(" "):
            word = word.replace("#", "")
            if word in poswords:
                tweets[index] += " _POSITIVE_"
            if word in negwords:
                tweets[index] += " _NEGATIVE_"

    print tweets

    # ZET IN VERSLAG DAT IK TRUMP HEB WEGGEHAALD UIT POSITIEVE WOORDEN LOL