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
        
def twitter_search_team(team):
    # create twitter API object
    twitter = set_api()
    team = remove_spec(team)
    results = twitter.users.search(q = '"' + team + '"')
    
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
    else:
        page_dict = {'twitter_name' : "NaN",
                     'twitter_id' : "NaN",
                     'twitter_followers' : "NaN",
                     'twitter_created_at' : "NaN",
                     'twitter_statuses' : "NaN",
                     'twitter_url' : "NaN"
                     }
        return page_dict
 
def get_twitter_name(team):
    results = twitter_search_team(team)
    return results['twitter_name']
    
def get_twitter_id(team):
    results = twitter_search_team(team)
    return results['twitter_id']
    
def get_twitter_followers(team):
    results = twitter_search_team(team)
    return results['twitter_followers']
    
def get_twitter_created_at(team):
    results = twitter_search_team(team)
    return results['twitter_created_at']
    
def get_twitter_statuses(team):
    results = twitter_search_team(team)
    return results['twitter_statuses']
       
def get_twitter_url(team):
    results = twitter_search_team(team)
    return results['twitter_url']