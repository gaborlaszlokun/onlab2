# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from facebook_search import *
from instagram_search import *
from twitter_search import *

def social_media_search(team):

    team_dict = instagram_search_team(team) 
    team_dict.update(twitter_search_team(team))
    team_dict.update(facebook_search_team(team))

    return team_dict
    
def print_result(team):
#    print (social_media_search(team))
    for key, value in social_media_search(team).items():
        print (key, ":", value)
        
def main_print(team):
    print(team)
    print(social_media_search(team)['instagram_name'])
    print (social_media_search(team)['instagram_id'])
    print(social_media_search(team)['facebook_name'])
    print (social_media_search(team)['facebook_id'])
    print(social_media_search(team)['twitter_name'])
    print (social_media_search(team)['twitter_id'])
    print()
    
    
