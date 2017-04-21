# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 14:21:09 2017

@author: ASUS
"""

import urllib2
import json

access_token = "614700401966588|7af8b0fda1b43f908b8853ed65e8b648"  # Access Token

def get_correct_page(page_id):
    api_endpoint = "https://graph.facebook.com/v2.4/"
    fb_graph_url = api_endpoint+page_id+"?fields=id,name,likes,link,talking_about_count,category&access_token="+access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

def get_page_data(team):
    team = team.replace(" ","%20")
    search = search_team(team)
    page_list = []
    for i in search['data']:
        page_data = get_correct_page(i['id'])
        page_tup = (page_data['name'], i['id'],  page_data['likes'], page_data['link'])
        page_list.append(page_tup)

    official_page = max(page_list,key=lambda item:item[2])
    page_json = get_correct_page(official_page[1])
    # TODO: format it to dict!
    page_tuple = (page_json['name'], page_json['id'], page_json['link'], page_json['likes'], page_json['talking_about_count'], page_json['category'])
    return page_tuple
            
def search_team(query):
    fb_graph_url = "https://graph.facebook.com/search?q=" + query + "&type=page&access_token=" + access_token
    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

def get_page_fans(query,access_token, start_date, final_date):
    fb_graph_url = "https://graph.facebook.com/v2.6/" + query + "/insights/page_fans_country/lifetime?&since=" + start_date + "&until=" + final_date + "&access_token=" + access_token

    try:
        api_request = urllib2.Request(fb_graph_url)
        api_response = urllib2.urlopen(api_request)
        
        try:
            return json.loads(api_response.read())
        except (ValueError, KeyError, TypeError):
            return "JSON error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
        elif hasattr(e, 'reason'):
            return e.reason

def get_name(team):
    return get_page_data(team)[0]
    
def get_id(team):
    return get_page_data(team)[1]
    
def get_link(team):
    return get_page_data(team)[2]

def get_likes(team):
    return get_page_data(team)[3]

def get_talking_about(team):
    return get_page_data(team)[4]   
    
def get_category(team):
    return get_page_data(team)[5]

# Some extra links

#link = "https://graph.facebook.com/DiamondPlatnumz255?access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648"
#https://graph.facebook.com/v2.6/204153042939851/posts/?fields=message,link,permalink_url,created_time,type,name,id,comments.limit(0).summary(true),shares,likes.limit(0).summary(true),reactions.limit(0).summary(true)&limit=100&access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648
#https://graph.facebook.com/search?q=manchester+united&type=page&access_token=614700401966588%7C7af8b0fda1b43f908b8853ed65e8b648
#https://graph.facebook.com/v2.6/barackobama/insights/page_fans_country/lifetime?&since=2016-06-01&until=2016-09-02&access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648
#https://graph.facebook.com/v2.6/7724542745/insights/page_fans_country/lifetime?&since=2016-06-01&until=2016-09-02&access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648
