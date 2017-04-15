# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from twitter import *
from spec_char_remover import remove_spec
import time

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)


def search_team(query):
    #-----------------------------------------------------------------------
    # create twitter API object
    #-----------------------------------------------------------------------
    twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))
    
    #-----------------------------------------------------------------------
    # perform a user search 5
    # twitter API docs: https://dev.twitter.com/rest/reference/get/users/search
    #-----------------------------------------------------------------------
    query = remove_spec(query)
    results = twitter.users.search(q = '"' + query + '"')
    
    #-----------------------------------------------------------------------
    # loop through each of the users, and print their details
    #-----------------------------------------------------------------------
    if len(results) >0:
        user = results[0]
        # Format the date into a correct form
        created_at = time.strftime('%Y-%m-%d', time.strptime(user["created_at"],'%a %b %d %H:%M:%S +0000 %Y'))
        return (user["screen_name"], user["id"], user["url"], created_at, user["followers_count"],user["statuses_count"])
    else:
        return ("NaN", "NaN", "NaN", "NaN", "NaN", "NaN")