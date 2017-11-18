# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:15:46 2017

@author: ASUS
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('football_data.db')
c = conn.cursor()

# Create table
try:
    c.execute('''CREATE TABLE main_teams
             (team_name text primary key, facebook_id real, twitter_id, instagram_id real)''')
except:
    None


main_teams = pd.read_csv('main_teams.csv')

for i in range(len(main_teams)):
    print(main_teams.loc[i,'query'],"|", main_teams.loc[i,'instagram_id'],"|", main_teams.loc[i,'instagram_name'])

#print(mdain_teams)
