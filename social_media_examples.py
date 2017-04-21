# -*- coding: utf-8 -*-
"""
@author: ASUS
"""

from social_media_search import  *

team = "feyenoord"

for key, value in social_media_search(team).iteritems():
    print key, ":", value