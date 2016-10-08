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

# Create another list to extra the User key from each entry which contains
# the value/Dictionary with our screen_name key
userData = []
for user in tweets:
    userData.append(user['user'])

# With our userData list now created, we can now iterate over it again with
# another for loop
screenNames= []
for name in userData:
    screenNames.append(name['screen_name'])

# Now that we have our two lists, a list of tweet text and screen names, we
# can use the zip() function to join the values from each and print that zipped
# list, giving us the user name followed by the tweet
joined = zip(screenNames, text)



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

print joined