"""
    This is a simple application to grab the links to various articles that someone has posted on Twitter.
    It is based on examples from Web Scraping with Python by Ryan Mitchell from O'Reilly Press.
    This program requires the twitter api which requires you to register an app.
    You can get a Twitter screen name at www.twitter.com and register the app at https://apps.twitter.com/app/
    Gerald Sears 5/13/16
"""
# TODO: Add cli interface to program.
# TODO: Add exception/error handling.

# Using Twitter Tools from http://mike.verdone.ca/twitter/#downloads
from twitter import Twitter, OAuth
import re

#   Set Access tokens here. Remember to put them in ''s.
AccessToken = 'Your Token Here'
AccessTokenSecret = 'Your Secret Here'
ConsumerKey = 'Your Key Here'
ConsumerSecret = 'Your Secret Here'

def getTweets(account,tweets):
    # Gets a number of status updates for a particular account.
    # account is the screen name you want, and tweets is the number of updates.
    # TODO: Find a way to set this up to pull tweets by date range.
    t = Twitter(auth=OAuth(AccessToken,AccessTokenSecret,ConsumerKey,ConsumerSecret))
    pythonStatuses = t.statuses.user_timeline(screen_name=account, count=tweets)
    return(pythonStatuses)

def getURLs(tweetsGot):
    # Searches each tweet for embedded URLs.  At the moment this only picks up the first URL.
    # TODO: Add support for multiple URLs.
    # TODO: Add return of URLs in list or dictionary possibly with the tweet they were found in.
    # TODO: Add URL checking.
    for index in range(len(tweetsGot)):
        print(tweetsGot[index]['text'])
        search = re.search("(?P<url>https?://[^\s]+)", tweetsGot[index]['text'])
        if search == None:
            print("No URLs Found.")
        else:
            print("Found: " + re.search("(?P<url>https?://[^\s]+)", tweetsGot[index]['text']).group("url"))

tweetsGot = getTweets('timoreilly',30)
getURLs(tweetsGot)