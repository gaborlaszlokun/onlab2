# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:38:18 2017

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


final_csv = "team_tw_name,tw_id,tw_link,followers\n"
for num in range(0,len(team_list)):
    team = team_list[num]
    team_tup = search_team(team)
    for i in team_tup:
        print i
    print
    """
    token = "614700401966588|7af8b0fda1b43f908b8853ed65e8b648"  # Access Token
    query = team_list[num].replace(" ","+")
    
    search = search_team(query,token)
    page_list = []
    for i in search['data']:
        page_data = get_page_data(i['id'],token)
        page_tup = (page_data['name'], i['id'],  page_data['likes'], page_data['link'])
        page_list.append(page_tup)
    
    official_page = max(page_list,key=lambda item:item[2])
    line = official_page[0] + "," + official_page[1] + "," + official_page[3] + "\n"
    print line
    line = smart_str(line)
    text = open("teams_fb.csv", "a")
    text.write(line)
    text.close()
    print num
    print team_list[num]
"""