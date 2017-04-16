# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:18:09 2017

@author: ASUS
"""

from instagram_search import search_team, get_followers

team = "Feyenoord"

team_tup = search_team(team)
print team 
for i in team_tup:
    print i
    
print get_followers(team), "followers"