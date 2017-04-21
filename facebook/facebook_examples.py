# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from facebook_crawler import search_team, get_page_data, get_likes
from django.utils.encoding import smart_str

team = "ferencváros"

for i in get_page_data(team):
    print i
 
print get_page_data(team)[0]   
print get_likes(team), "kedvelés"



