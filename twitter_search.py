# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from twitter import *
from spec_char_remover import remove_spec
import time
import urllib2

def set_api(): 
    config = {}
    execfile("twitter_config.py", config)
    api = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
    return api
        
def twitter_search_team(query):
    # create twitter API object
    twitter = set_api()
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
        page_dict = {'twitter_name' : user["screen_name"],
                     'twitter_id' : user["id"],
                     'twitter_followers' : user["followers_count"],
                     'twitter_created_at' : created_at,
                     'twitter_statuses' : user["statuses_count"],
                     'twitter_url' : url
                     }
        return page_dict
        return (user["screen_name"], user["id"], url, created_at, user["followers_count"],user["statuses_count"])
    else:
        return ("NaN", "NaN", "NaN", "NaN", "NaN", "NaN")
        
def get_followers(query):
    twitter = set_api()
    results = twitter.users.search(q = '"' + query + '"')
    
    if len(results) > 0:
        user = results[0]
        return user["followers_count"]
    else:
        return "NaN"