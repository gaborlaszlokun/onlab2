# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:28:51 2017

@author: ASUS
"""
import datetime
from datetime import date
from facebook_crawler import get_page_fans

query = "fradi.hu"
token = "614700401966588|7af8b0fda1b43f908b8853ed65e8b648"  # Access Token

base_date = date(2015, 3, 11)#.isoformat()
for i in range(734):
    start_date = base_date + datetime.timedelta(days=i)
    final_date = start_date + datetime.timedelta(days=1)
#    print start_date, final_date
    prefix = get_page_fans(query, token, str(start_date), str(final_date))['data'][0]['values']
   
    sum = 0
    for i in prefix[0]['value']:
        sum += prefix[0]['value'][i]
    print prefix[0]['end_time'][0:10], sum
    line = prefix[0]['end_time'][0:10] + "\n"
    text = open("teams_dates.csv", "a")
    text.write(line)
    text.close()