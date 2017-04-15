# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 14:21:09 2017

@author: ASUS
"""

#link = "https://graph.facebook.com/DiamondPlatnumz255?access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648"
#https://graph.facebook.com/v2.6/204153042939851/posts/?fields=message,link,permalink_url,created_time,type,name,id,comments.limit(0).summary(true),shares,likes.limit(0).summary(true),reactions.limit(0).summary(true)&limit=100&access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648

import urllib2
import json

def get_page_data(page_id,access_token):
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
            
def search_team(query,access_token):
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

def get_likes(page_id, access_token):
    return get_page_data(page_id, token)['likes']

def get_id(page_name, access_token):
    return get_page_data(page_name, token)['id']
    
def get_name(page_id, access_token):
    return get_page_data(page_id, token)['name']
    
def get_category(page_id, access_token):
    return get_page_data(page_id, token)['category']

query = "fkaustria"
token = "614700401966588|7af8b0fda1b43f908b8853ed65e8b648"  # Access Token


#print len(get_page_fans(query, token, "2015-03-11", "2015-03-14")['data'][0]['values'])
#sum = 0
#for i in get_page_fans(query, token, "2015-03-11", "2015-03-14")['data'][0]['values'][0]['value']:
#    sum += get_page_fans(query, token, "2015-03-11", "2015-03-14")['data'][0]['values'][0]['value'][i]
#print sum


#print get_id(query, token)
#print get_category(query, token)

#query = query.replace(" ","+")

#page_id = "DiamondPlatnumz255"
#page_id = "7724542745"

#page_data = get_likes(page_id,token)
#print page_data
#print "Page Name:"+ page_data['name']
#print "Likes:"+ str(page_data['likes'])
#print "Link:"+ page_data['link']
#print "Talking about:" + str(page_data['talking_about_count'])
#print


"""
search = search_team(query,token)
page_list = []
for i in search['data']:
    page_data = get_page_data(i['id'],token)
#    print i['id'], page_data['name'], page_data['likes'], page_data['link']
    page_tup = (i['id'], page_data['name'], page_data['likes'], page_data['link'])
    page_list.append(page_tup)

official_page = max(page_list,key=lambda item:item[2])
for item in official_page:
    print item
"""


#https://graph.facebook.com/search?q=manchester+united&type=page&access_token=614700401966588%7C7af8b0fda1b43f908b8853ed65e8b648
#https://graph.facebook.com/v2.6/barackobama/insights/page_fans_country/lifetime?&since=2016-06-01&until=2016-09-02&access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648
#https://graph.facebook.com/v2.6/7724542745/insights/page_fans_country/lifetime?&since=2016-06-01&until=2016-09-02&access_token=614700401966588|7af8b0fda1b43f908b8853ed65e8b648
