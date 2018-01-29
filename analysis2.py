import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

tweets_data_path = 'tweetdata.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
#print(tweets_data)
print(len(tweets_data))
sent = pd.read_excel('sentiment2.xlsx')
print(sent.head())
print(sent['id'])
print(len(sent))

x = []
y = []
for i in range(len(tweets_data)):
    if tweets_data[i]['id']==sent['id'][i]:
        x.append(tweets_data[i]['text'])
        y.append(sent['sentiment'][i])
print(x[0].split(" "))
print(y[0])
vectorizer = CountVectorizer(stop_words='english')
train_features = vectorizer.fit_transform(x)
#print(train_features)
actual = y[:-1500]



nb = MultinomialNB()
nb.fit(train_features, [int(r) for r in y])

test_features = vectorizer.transform(x[:-1500])
test_try= vectorizer.transform(["Can we all stop treating anxiety like it's a choice and something cool to have thank you"])
test_try2= vectorizer.transform(["I want to die depression sucks"])
predict2 = nb.predict(test_try)
predict3 = nb.predict(test_try2)

#print(predict2)
predictions = nb.predict(test_features)

print()

fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
print("Multinomial naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))

print(predict2)
print(predict3)
