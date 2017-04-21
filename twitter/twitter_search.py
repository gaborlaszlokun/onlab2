# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from twitter import *
from spec_char_remover import remove_spec
import time
import urllib2

# load our API credentials 
config = {}
execfile("twitter_config.py", config)
    
def search_team(query):
    # create twitter API object
    twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
    query = remove_spec(query)
    results = twitter.users.search(q = '"' + query + '"')
    
    if len(results) > 0:
        user = results[0]
        # Expand the urls
        try:
            tco_url = user["url"]
            req = urllib2.urlopen(tco_url)
            url = req.url
        except:
            url = "NaN"
        # Format the date into a correct form
        created_at = time.strftime('%Y-%m-%d', time.strptime(user["created_at"],'%a %b %d %H:%M:%S +0000 %Y'))
        return (user["screen_name"], user["id"], url, created_at, user["followers_count"],user["statuses_count"])
    else:
        return ("NaN", "NaN", "NaN", "NaN", "NaN", "NaN")
        
def get_followers(query):
    twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
    query = remove_spec(query)
    results = twitter.users.search(q = '"' + query + '"')
    
    if len(results) > 0:
        user = results[0]
        return user["followers_count"]
    else:
        return "NaN"