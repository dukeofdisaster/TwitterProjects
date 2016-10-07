# Analyze Tweets
import json
from pprint import pprint

tweets = []
for line in open('/home/jmo/gitprojects/TwitterProject/initialdata.json', 'r'):

    try:
        tweets.append(json.loads(line))
    except:
        pass

# Now we simply take the length of entries in our .json file
print"Number of Tweets found:"
print len(tweets)
print

#We create a new list and append all the entries under tweet['text']
text = []
for tweet in tweets:
    text.append(tweet['text'])

# Create another list for handling screen names
screenNames = []
for tweet in tweets:
    screenNames.append(tweet['screen_name'])

print "Number of text entries found"
print len(text)
print "---------"
print "Below are the text entries found:"
print "---------------------------------"

# Now we create an integer variable to increment that way we can print out
# All the tweets in our list with numbers. We initialize this variable with
# The value 1 so it starts counting regulary rather than at 0
newTweet = 1

# We loop through the text list, or our list of tweets
for i in text:
    print "Tweet #", newTweet
    print "======="
    print(i + "\n")
    print "----------"
    newTweet += 1

for user in screenNames:
    print user