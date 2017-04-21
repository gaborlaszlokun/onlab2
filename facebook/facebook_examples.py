# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from facebook_search import *

team = "ferencváros"

for i in get_page_data(team):
    print i
 
print get_page_data(team)[0]   
print get_likes(team), "kedvelés"



