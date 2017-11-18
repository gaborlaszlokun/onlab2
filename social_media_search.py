# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from facebook_search import *
from instagram_search import *
from twitter_search import *

def social_media_search(team_alts):

    team_dict = facebook_search_team(team_alts[0])
    team_dict.update(twitter_search_team(team_alts[1]))
    team_dict.update(instagram_search_team(team_alts[2]))

    return team_dict
    
def print_result(team):
#    print (social_media_search(team))
    for key, value in social_media_search(team).items():
        print (key, ":", value)
        
def main_print(team):
    print(team)
    print(social_media_search(team)['facebook_likes'])
    print(social_media_search(team)['instagram_followers'])
    print(social_media_search(team)['twitter_followers'])
    print()
    
def save_main_teams(team):
    raise NotImplementedError
