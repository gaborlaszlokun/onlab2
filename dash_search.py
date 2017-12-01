# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 21:56:28 2017

@author: ASUS
"""

#python.exe "C:\Users\ASUS\Documents\Python Scripts\onlab2\dash_search.py"

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
from social_media_search import  *
import pandas as pd

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='input-1-state', type="text", value='ferencvaros'),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])


@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value')])
def update_output(n_clicks, team):
#    return u'''
#        Input 1 is "{}"
#    '''.format(str(social_media_search(team)['facebook_name']))
    search = social_media_search(team)
    return html.Div([
        html.H3(search['facebook_name']),
        html.H3(search['facebook_likes'])
    ])


if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=801)
    
    




#print(social_media_search(team))

#for key, value in social_media_search(team).items():
#    print (key, ":", value)