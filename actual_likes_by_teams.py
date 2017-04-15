# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 23:36:11 2017

@author: ASUS
"""

import pandas as pd
from facebook_crawler import get_likes, get_category
from django.utils.encoding import smart_str

teams = pd.read_csv("teams_fb.csv")
token = "614700401966588|7af8b0fda1b43f908b8853ed65e8b648"  # Access Token

teams['category'] = teams.apply(lambda row: get_category(str(row[1]), token), axis=1)
teams['likes'] = teams.apply(lambda row: get_likes(str(row[1]), token), axis=1)
#teams = teams[teams['likes'] >= 100000].reset_index(drop=True)
print teams
teams.to_csv('actual_likes.csv', sep=',', encoding='utf-8')


#for i in range(len(teams)):
#    likes = get_likes(str(teams.iat[i,1]), token)
#    if likes > 100000:
#        print teams.iat[i,0], ":", likes