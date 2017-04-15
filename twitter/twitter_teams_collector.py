# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 19:39:31 2017

@author: ASUS
"""

import pandas as pd
from twitter_search import search_team
from django.utils.encoding import smart_str

teams = pd.read_csv("teams.csv")
team_list = teams['team_name']
#team_list = ["Diósgyőri vtk"]

header = "team_name,team_tw_name,tw_id,url,created_at,followers,statuses\n"
text = open("teams_twitter.csv", "a")
text.write(header)
text.close()
for num in range(0,len(team_list)):
    team = team_list[num]
    team_tup = search_team(team)
    
    line = team
    for i in team_tup:
        line += "," + str(i)
    line += "\n"
    print line
    line = smart_str(line)
    text = open("teams_twitter.csv", "a")
    text.write(line)
    text.close()
