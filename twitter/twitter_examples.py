# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from twitter_search import search_team, get_followers

team = "Feyenoord"

team_tup = search_team(team)
print team 
for i in team_tup:
    print i
    
print get_followers(team), "followers"