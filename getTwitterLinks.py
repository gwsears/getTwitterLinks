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

#  Target settings
accountName = 'timoreilly'
numbToGet = 30

def getTweets(account,tweets):
    # Gets a number of status updates for a particular account.
    # account is the screen name you want, and tweets is the number of updates.
    # Returns a twitter status object with 1 or more tweets.
    # TODO: Find a way to set this up to pull tweets by date range.
    t = Twitter(auth=OAuth(AccessToken,AccessTokenSecret,ConsumerKey,ConsumerSecret))
    pythonStatuses = t.statuses.user_timeline(screen_name=account, count=tweets)
    return(pythonStatuses)

def getURLs(tweetsGot):
    # Searches each tweet for embedded URLs.  At the moment this only picks up the first URL.
    # TODO: Add URL checking.
    listURLs = []  # entered as [{'text':'tweet text', 'urlsFound':Boolean, urls:['URL1', 'URL2']}]
    for index in range(len(tweetsGot)):
        #print(tweetsGot[index]['text'])
        listURLs.append({'text':tweetsGot[index]['text']})
        search = re.search("(?P<url>https?://[^\s]+)", tweetsGot[index]['text'])
        if search == None:
            #print("No URLs Found.")
            listURLs[index]['urlsFound'] = False
            listURLs[index]['urls'] = []
        else:
            listURLs[index]['urlsFound'] = True
            foundURLs = re.findall("(?P<url>https?://[^\s]+)", tweetsGot[index]['text'])
            #print(foundURLs)
            listURLs[index]['urls'] = foundURLs
            #print("Found: " + re.search("(?P<url>https?://[^\s]+)", tweetsGot[index]['text']).group("url"))
    #print(listURLs)
    return listURLs

tweetsGot = getTweets(accountName,numbToGet)
print(tweetsGot)
urlsGot = getURLs(tweetsGot)
print("* * * * Here's the URLs pulled with each tweet. * * * *")
print(urlsGot)

for index in range(len(urlsGot)):
    print('This tweet: ' + urlsGot[index]['text'])
    if urlsGot[index]['urlsFound'] == True:
        print('  has the following URLs: ' + str(urlsGot[index]['urls']))
    else:
        print('  has no URLs.')