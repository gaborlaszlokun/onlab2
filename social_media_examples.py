# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from social_media_search import  *
import pandas as pd

team = "1899 Hoffenheim"

#for key, value in social_media_search(team).iteritems():
#    print key, ":", value
    
#print_result(team)

teams = pd.read_csv("main_teams_list.csv")

for i in range(len(teams)):
    team = teams.iat[i,0]
    print_result(team)
