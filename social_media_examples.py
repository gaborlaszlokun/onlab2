# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from social_media_search import  *
import pandas as pd

#team = "udlaspalmasoficial"

#print(social_media_search(team))

#for key, value in social_media_search(team).items():
#    print (key, ":", value)

#social_media_search(team)['instagram_name']
#social_media_search(team)['instagram_id']
   
#print_result(team)

"""
teams = pd.read_csv("main_teams.csv")

columns = ['query', 'facebook_likes', 'twitter_followers', 'instagram_followers']
main_teams_df = pd.DataFrame(columns=columns)
index = 0
for i in range(len(teams)):
    team = teams.loc[i,'query']
    team_alts = (teams.loc[i,'facebook_name'],teams.loc[i,'twitter_name'],teams.loc[i,'instagram_name'])
    print (team_alts)
    result = social_media_search(team_alts)
#    print (result)
    facebook_likes = result['facebook_likes']
    twitter_followers = result['twitter_followers']
    instagram_followers = result['instagram_followers']

    
    main_teams_line = pd.DataFrame([[team,facebook_likes, twitter_followers, instagram_followers]], columns=columns, index = [index])
    index += 1
    main_teams_df = main_teams_df.append(main_teams_line)
    main_teams_df.to_csv("main_teams_meas.csv", sep=',', encoding='utf-8', index=False) 
    


"""
teams_meas = pd.read_csv("main_teams_meas.csv")

for i in range(len(teams_meas)):
    if teams_meas.loc[i,'facebook_likes'] < 10000 or teams_meas.loc[i,'twitter_followers'] < 10000 or teams_meas.loc[i,'instagram_followers'] < 10000:
        print (teams_meas.loc[i,'query'],teams_meas.loc[i,'facebook_likes'], teams_meas.loc[i,'twitter_followers'], teams_meas.loc[i,'instagram_followers'])
        