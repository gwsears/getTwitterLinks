"""
    This is a simple application to grab the links to various articles that someone has posted on Twitter.
    It is based on examples from Web Scraping with Python by Ryan Mitchell from O'Reilly Press.
    This program requires the twitter api which requires you to register an app.
    You can get a Twitter screen name at www.twitter.com and register the app at https://apps.twitter.com/app/
    Gerald Sears 5/13/16
"""
# TODO: Add cli interface to program.
# TODO: Add exception/error handling.
# TODO: Add export urls/emails to file, perhaps csv.
# TODO: Build function to print out results.
# TODO: Add GUI interface.
# TODO: Setup as stand-alone program.

# Using Twitter Tools from http://mike.verdone.ca/twitter/#downloads
from twitter import Twitter, OAuth
import re

#   Set Access tokens here. Remember to put them in ''s.
AccessToken = 'Your Token Here'
AccessTokenSecret = 'Your Secret Here'
ConsumerKey = 'Your Key Here'
ConsumerSecret = 'Your Secret Here'

#  Target settings
accountName = 'geraldwsears'
numbToGet = 3

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
    # TODO: Figure out if there is a better way to pull URLs & if I'm getting the whole URL.
    # TODO: Embedded media isn't getting captured very well.  URLs shortened, need to figure out how to fix.
    listURLs = []  # entered as [{'text':'tweet text', 'urlsFound':Boolean, urls:['URL1', 'URL2']}]
    for index in range(len(tweetsGot)):
        listURLs.append({'text':tweetsGot[index]['text']})
        search = re.search("(?P<url>https?://[^\s]+)", tweetsGot[index]['text'])
        if search == []:
            listURLs[index]['urlsFound'] = False
            listURLs[index]['urls'] = []
        else:
            listURLs[index]['urlsFound'] = True
            foundURLs = re.findall("(?P<url>https?://[^\s]+)", tweetsGot[index]['text'])
            listURLs[index]['urls'] = foundURLs
    return listURLs

def getEmails(tweetsGot):
    # Searches each tweet for emails contained in the text of the tweet.
    listEmails = [] # [{'text':'tweet text','emailsFound':Boolean,emails:[emaila,emailb...]}]
    test = []
    for index in range(len(tweetsGot)):
        search = re.findall("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",tweetsGot[index]['text'])
        print("This search for index" + str(index))
        print(search)
        if search == test:
            listEmails.append({'text': tweetsGot[index]['text']})
            listEmails[index]['emailsFound'] = False
        else:
            listEmails.append({'text': tweetsGot[index]['text']})
            listEmails[index]['emailsFound'] = True
            foundEmails = re.findall("[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}",tweetsGot[index]['text'],re.IGNORECASE)
            listEmails[index]['emails'] = foundEmails
    return listEmails

tweetsGot = getTweets(accountName,numbToGet)
emailsGot = getEmails(tweetsGot)
# This is a check on data being collected with the URLs being pulled by our regular expression.
print("* * * * Here's the URLs pulled with each tweet. * * * *")
print(emailsGot)

# This is a printout closer to something useable.
for index in range(len(emailsGot)):
    print('This tweet: ' + emailsGot[index]['text'])
    if emailsGot[index]['emailsFound'] == True:
        print('  has the following emails: ' + str(emailsGot[index]['emails']))
    else:
        print('  has no emails.')