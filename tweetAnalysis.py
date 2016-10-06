# Analyze Tweets
import json
from pprint import pprint

tweets = []
for line in open('/home/jmo/gitprojects/TwitterProject/initialdata.json', 'r'):

    try:
        tweets.append(json.loads(line))
    except:
        pass

print"Number of Tweets found:"
print len(tweets)
print

text = []
for tweet in tweets:
    text.append(tweet['text'])

print "Number of text entries found"
print len(text)
print text
for i in text:
    print i +"\n"