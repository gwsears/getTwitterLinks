"""
    This is a simple application to grab the links to various articles that someone has posted on Twitter.
    It is based on examples from Web Scraping with Python by Ryan Mitchell from O'Reilly Press.
    Gerald Sears 5/12/16
"""

from twitter import Twitter, OAuth
import re

#   Set Access tokens here.
AccessToken = 'Your Token Here'
AccessTokenSecret = 'Your token here'
ConsumerKey = 'your token here'
ConsumerSecret = 'your token here'

def getTweets(account,tweets):
    # Gets a number of status updates for a particular account.
    # account is the screen name you want, and tweets is the number of updates.
    t = Twitter(auth=OAuth(AccessToken,AccessTokenSecret,ConsumerKey,ConsumerSecret))
    pythonStatuses = t.statuses.user_timeline(screen_name=account, count=tweets)
    #print("------pythonStatuses------")
    #print(pythonStatuses)
    return(pythonStatuses)

tweetsGot = getTweets('timoreilly',30)

print(type(tweetsGot))

for index in range(len(tweetsGot)):
    print(index)
    print(tweetsGot[index]['text'])
    #print(re.search("(?P<url>https?://[^\s]+)", tweetsGot[index]['text']).group("url"))

print("***********Get the URLs**********")
for index in range(len(tweetsGot)):
    print(tweetsGot[index]['text'])
    print(re.search("(?P<url>https?://[^\s]+)", tweetsGot[index]['text']).group("url"))