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
             (team_name text primary key, facebook_name text, twitter_name text, instagram_name text)''')
except:
    None


main_teams = pd.read_csv('main_teams.csv')

teams = []
for i in range(len(main_teams)):
    
    team_tuple = ((main_teams.loc[i,'query'], main_teams.loc[i,'facebook_name'], main_teams.loc[i,'twitter_name'] , main_teams.loc[i,'instagram_name']))
    teams.append(team_tuple)
#print (teams)
try:
    c.executemany('INSERT INTO main_teams VALUES (?,?,?,?)', teams)
    # Save (commit) the changes
    conn.commit()
except:
    None
    
c.execute('SELECT * FROM main_teams')
print(c.fetchall())

conn.close()  
