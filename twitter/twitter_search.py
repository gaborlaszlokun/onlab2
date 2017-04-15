# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:00:14 2017

@author: ASUS
"""

from twitter import *

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
    results = twitter.users.search(q = '"' + query + '"')
    
    #-----------------------------------------------------------------------
    # loop through each of the users, and print their details
    #-----------------------------------------------------------------------
    if len(results) >0:
        user = results[0]
        return (query, user["screen_name"], user["id"], user["url"], user["followers_count"], user["created_at"], user["statuses_count"])
    else:
        return (query, "NaN", "NaN", "NaN", "NaN", "NaN", "NaN")
#    for user in results:
    #    print user
    #    print
#        print "@%s (%s): %s" % (user["screen_name"], user["name"], user["followers_count"])