# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from facebook_search import *
from instagram_search import *
from twitter_search import *

def social_media_search(team):

    team_dict = dict(instagram_search_team(team).items() + twitter_search_team(team).items() +  facebook_search_team(team).items())
    return team_dict
    