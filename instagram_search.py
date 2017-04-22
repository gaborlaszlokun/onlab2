# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from instagram import InstagramAPI
from spec_char_remover import remove_spec

def set_api():
    config = {}
    execfile("instagram_config.py", config)
    api = InstagramAPI(client_id=config['client_id'], client_secret=config['client_secret'], access_token=config['access_token'])
    return api

def instagram_search_team(query):
    api = set_api()
    user_name = remove_spec(query)
    try:
        search_result = api.user_search(q=user_name)
        user = api.user(search_result[0].id)
        page_dict = {'instagram_name' : user.username,
                     'instagram_id': user.id,
                     'instagram_media': user.counts['media'],
                     'instagram_followers': user.counts['followed_by'],
                     'instagram_follows' : user.counts['follows'],
                     'instagram_url' : user.website}
        return page_dict

    except:
        page_dict = {'instagram_name' : "NaN",
                     'instagram_id': "NaN",
                     'instagram_media': "NaN",
                     'instagram_followers': "NaN",
                     'instagram_follows' : "NaN",
                     'instagram_url' : "NaN"}
        return page_dict
 
def get_instagram_name(team):
    result = instagram_search_team(team)
    return result['instagram_name']
    
def get_instagram_id(team):
    result = instagram_search_team(team)
    return result['instagram_id']
    
def get_instagram_media(team):
    result = instagram_search_team(team)
    return result['instagram_media']
       
def get_instagram_followers(team):
    result = instagram_search_team(team)
    return result['instagram_followers']
    
def get_instagram_follows(team):
    result = instagram_search_team(team)
    return result['instagram_follows']
    
def get_instagram_url(team):
    result = instagram_search_team(team)
    return result['instagram_url']
