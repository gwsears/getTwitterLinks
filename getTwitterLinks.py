"""
    This is a simple application to grab the links to various articles that someone has posted on Twitter.
    It is based on examples from Web Scraping with Python by Ryan Mitchell from O'Reilly Press.
    Gerald Sears 5/12/16
"""

from twitter import Twitter, OAuth

#   Set Access tokens here.
AccessToken = '4440695914-mL3peFV4ifwF4P5B0rdleJxVwsKcJHuNmeRKB1k'
AccessTokenSecret = 'mr6NqYZXTSPzmqAjF3LgqFadFY0SWElXDctog1G1FwDSA'
ConsumerKey = 'WzDrJzcemyo3Jx0uYOBPflPNB'
ConsumerSecret = 'v6zAcsBKWeQO8fZ08AAbukDn5R8E8BcTTViI5Iq7kOGKAfXtO3'

def getTweets(account,tweets):
    # Gets a number of status updates for a particular account.
    # account is the screen name you want, and tweets is the number of updates.
    t = Twitter(auth=OAuth(AccessToken,AccessTokenSecret,ConsumerKey,ConsumerSecret))
    pythonStatuses = t.statuses.user_timeline(screen_name=account, count=tweets)
    print(pythonStatuses)

getTweets('engadget',5)