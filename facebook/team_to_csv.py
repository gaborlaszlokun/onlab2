# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:00:36 2017

@author: ASUS
"""

import pandas as pd
from facebook_crawler import get_likes, get_category
from django.utils.encoding import smart_str
import datetime
from datetime import date
from facebook_crawler import get_page_fans
import matplotlib.pyplot as plt


csv = pd.read_csv("teams_dates.csv")
team_name = "Juventus"

def add_team(team_name,base_date):
    query = team_name
    token = "614700401966588|7af8b0fda1b43f908b8853ed65e8b648"  # Access Token

#    base_date = date(2015, 3, 11)#.isoformat()
#    base_date = date(base_date)
    base_date =  datetime.datetime.strptime(base_date, "%Y-%m-%d")
#    for i in range(734):
    start_date = base_date
    final_date = start_date + datetime.timedelta(days=1)
    prefix = get_page_fans(query, token, str(start_date)[:10], str(final_date)[:10])['data'][0]['values']
        
    sum = 0
    for i in prefix[0]['value']:
        sum += prefix[0]['value'][i]
    print start_date, sum
    return sum
#token = "614700401966588|7af8b0fda1b43f908b8853ed65e8b648"  # Access Token



#csv[team_name] = csv.apply(lambda row: add_team(team_name, row[0]), axis=1)

col_list = ['date']
col_list +=sorted(list(csv.columns)[1:])
#col_list = col_list.remove("fcbayern")
print col_list
csv = csv[col_list]
print csv
csv.plot(x='date', figsize=(8, 5), legend = None)
# TODO: legendet máshova tenni

#csv.to_csv('teams_dates.csv', sep=',', encoding='utf-8', index=False)