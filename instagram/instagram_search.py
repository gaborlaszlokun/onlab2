# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from instagram import InstagramAPI
from spec_char_remover import remove_spec


client_id = "fb0a9594fbe14e72990c716c33b3f1d7"
client_secret = "c79a43ed0e8441c2a0ff7b2cc11b9e4a"
access_token = "2263070228.e029fea.1c3fc5838aea4f5685f9a5964ed36e7e"

# How to get access token:
#https://instagram.com/oauth/authorize/?client_id=fb0a9594fbe14e72990c716c33b3f1d7&redirect_uri=http://localhost&response_type=token

def search_team(query):
    api = InstagramAPI(client_id=client_id, client_secret=client_secret, access_token=access_token)
    user_name = remove_spec(query)
    try:
        search_result = api.user_search(q=user_name)
        user = api.user(search_result[0].id)
        return (query, user.id, user.username, user.full_name, user.website, user.counts['media'], user.counts['followed_by'], user.counts['follows'])

    except:
#        print user_name
        return (query, "NaN", "NaN", "NaN", "NaN", "NaN", "NaN", "NaN")
        