# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

import pandas as pd
from instagram_search import search_team
from django.utils.encoding import smart_str
from spec_char_remover import remove_spec

teams = pd.read_csv("teams.csv")
team_list = teams['team_name']
#team_list = ['ujpestfc']


final_csv = "team_name,insta_id,ista_name,insta_fullname,website,media_count,followed_by,follows\n"
for num in range(0,len(team_list)):
    team = team_list[num]
    
    team_tup = search_team(team)
    for i in team_tup:
        print i
        #TODO: csv generate
    print