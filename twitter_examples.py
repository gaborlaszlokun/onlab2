# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from twitter_search import *

team = "AEP Iraklis FC"

team_dict = twitter_search_team(team)
print team_dict
    
print get_twitter_name(team)
print get_twitter_id(team)
print get_twitter_followers(team)
print get_twitter_created_at(team)
print get_twitter_statuses(team)
print get_twitter_url(team)