# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from facebook_search import *

team = "arsenal"
 
for i  in facebook_search_team(team):
    print i

#filename = "main_teams_list.csv"
#facebook_generate_csv(filename)
