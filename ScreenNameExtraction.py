# screen name extraction
import json

tweets = []
for line in open('/home/jmo/gitprojects/TwitterProject/initialdata.json', 'r'):

    try:
        tweets.append(json.loads(line))
    except:
        pass

# OK Now we have to get creative. All we've done so far is import our entire
# JSON file into a python list. But it's messy as hell. It's a list of
# dictionaries and lists within a list. List-CEPTION! Anyways...


# 1: We create a new list called text to extract the values from the 'user' key
# in our in our tweets list/dictionary. Try and print out the new list. You'll
# know you've done it correctly if each dictionary in your text[] list of
# dictionaries starts with {u'follow_request_sent: None
text = []
for tweet in tweets:
    text.append(tweet['user'])


# 2: Now that we've created a new list of just the values for 'user', now we
#    can iterate over that list and pull out the values for the key 'screen_name'
screenNames = []
for name in text:
    screenNames.append(name['screen_name'])

print screenNames