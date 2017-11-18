# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from facebook_search import *

team = "Losc"
 
    
for key, value in facebook_search_team(team).items():
        print (key, ":", value)

#print(facebook_search_team(team))

#filename = "main_teams_list.csv"
#generate_facebook_csv(filename)
