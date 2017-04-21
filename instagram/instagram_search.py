# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from instagram import InstagramAPI
from spec_char_remover import remove_spec

# load our API credentials 
config = {}
execfile("instagram_config.py", config)

# How to get access token:
#https://instagram.com/oauth/authorize/?client_id=fb0a9594fbe14e72990c716c33b3f1d7&redirect_uri=http://localhost&response_type=token

def search_team(query):
    api = InstagramAPI(client_id=config['client_id'], client_secret=config['client_secret'], access_token=config['access_token'])
    user_name = remove_spec(query)
    try:
        search_result = api.user_search(q=user_name)
        user = api.user(search_result[0].id)
        return (user.username, user.id, user.counts['media'], user.counts['followed_by'], user.counts['follows'], user.website)

    except:
        return ("NaN", "NaN", "NaN", "NaN", "NaN", "NaN")
        
def get_followers(query):
    api = InstagramAPI(client_id=config['client_id'], client_secret=config['client_secret'], access_token=config['access_token'])
    user_name = remove_spec(query)
    try:
        search_result = api.user_search(q=user_name)
        user = api.user(search_result[0].id)
        return user.counts['followed_by']

    except:
        return "NaN"
        