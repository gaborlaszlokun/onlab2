# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from facebook_search import *

team = "fcbarcelona"
 
    
for key, value in facebook_search_team(team).iteritems():
        print key, ":", value

#filename = "main_teams_list.csv"
#generate_facebook_csv(filename)
