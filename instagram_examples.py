# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from instagram_search import *

team = "újpest"

team_dict = instagram_search_team(team)
print team_dict
 
print get_instagram_name(team)
print get_instagram_id(team)
print get_instagram_media(team)
print get_instagram_followers(team)
print get_instagram_follows(team)
print get_instagram_url(team)