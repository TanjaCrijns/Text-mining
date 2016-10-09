import numpy as np
import pandas, re, sklearn
from sklearn.cross_validation import KFold
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier

if __name__ == "__main__":
    with open("D:/Users/Tanja/Documents/Master/Text-Mining/Assignment5/files/negative_words.txt", "r") as f:
        negwords = [word[:-1] for word in f.readlines()]
        f.close()
    with open("D:/Users/Tanja/Documents/Master/Text-Mining/Assignment5/files/positive_words.txt", "r") as f:
        poswords = [word[:-1] for word in f.readlines()]
        f.close()
    df = pandas.read_excel("D:/Users/Tanja/Documents/Master/Text-Mining/Assignment5/files/tweets.xlsx")
    tweets = np.asarray(df['Tweet'])
    labels = np.asarray(df['Manual Annotation'])
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

    tweets = [re.sub('([a-z0-9])([A-Z])', r'\1 \2', tweet) for tweet in tweets]
    tweets = [tweet.lower() for tweet in tweets]
    tweets = [re.sub (r'[^\w\s]', "", tweet) for tweet in tweets]
    # for index in range(len(tweets)):
    #     for word in tweets[index].split(" "):
    #         word = word.replace("#", "")
    #         if word in poswords:
    #             tweets[index] += " _POSITIVE_"
    #         if word in negwords:
    #             tweets[index] += " _NEGATIVE_"

    kf = KFold(len(tweets), n_folds=10, shuffle=False)
    f1_score_weighted_list = []
    recall_list = []
    precision_list = []
    accuracy_list = []
    total_predictions = []
    for train, test in kf:
        print "Vectorizing"
        v = CountVectorizer()
        #v = TfidfVectorizer()
        train_text = [tweets[i] for i in train]
        test_text = [tweets[i] for i in test]
        X_train  = v.fit_transform(train_text)
        X_test = v.transform(test_text)
        y_train = labels[train]
        y_test = labels[test]
        #clf = MultinomialNB()
        #clf = SGDClassifier(random_state=0)
        clf = LogisticRegression()

        print "Fitting"
        clf.fit(X_train, y_train)


        predictions = clf.predict(X_test)
        accuracy = metrics.accuracy_score(y_test, predictions, normalize=True, sample_weight=None)
        accuracy_list.append(accuracy)
        f1_score_weighted = metrics.f1_score(y_test, predictions, average='weighted', sample_weight=None)
        f1_score_weighted_list.append(f1_score_weighted)
        recall = metrics.recall_score(y_test, predictions, pos_label=1, average='weighted', sample_weight=None)
        recall_list.append(recall)
        precision = sklearn.metrics.precision_score(y_test, predictions, pos_label=1, average='weighted', sample_weight=None)
        precision_list.append(precision)

        print metrics.classification_report(y_test, predictions, target_names=["neutral", "positive", "negative"])
        total_predictions = total_predictions + list(predictions)
    overall_accuracy = np.mean(accuracy_list)
    overall_f1_weighted = np.mean(f1_score_weighted_list)
    overall_recall = np.mean(recall_list)
    overall_precision = np.mean(precision_list)

    print "Accuracy=", overall_accuracy, "\n", "Weighted f1=", overall_f1_weighted, "\n", "Recall=", overall_recall, "\n", "Precision=", overall_precision

    df.append(total_predictions)
    df.to_excel("tweets.xlsx")
