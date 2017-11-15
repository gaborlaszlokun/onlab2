# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from social_media_search import  *
import pandas as pd

team = "real madrid"

#print(social_media_search(team))

#for key, value in social_media_search(team).items():
#    print (key, ":", value)

#social_media_search(team)['instagram_name']
#social_media_search(team)['instagram_id']
   
#print_result(team)

columns = ['query', 'facebook_name', 'facebook_id', 'twitter_name', 'twitter_id', 'instagram_name', 'instagram_id']
main_teams_df = pd.DataFrame(columns=columns)
index = 0

teams = pd.read_csv("main_teams_list.csv")

for i in range(len(teams)):
    team = teams.iat[i,0]
    
    result = social_media_search(team)
    print (result)
    facebook_name = result['facebook_name']
    facebook_id = result['facebook_id']
    twitter_name = result['twitter_name'] 
    twitter_id = result['twitter_id']
    instagram_name = result['instagram_name']
    instagram_id = result['instagram_id']
    
    main_teams_line = pd.DataFrame([[team,facebook_name, facebook_id, twitter_name, twitter_id, instagram_name, instagram_id]], columns=columns, index = [index])
    index += 1
    main_teams_df = main_teams_df.append(main_teams_line)
    
main_teams_df.to_csv("main_teams.csv", sep=',', encoding='utf-8', index=False)
    
