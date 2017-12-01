# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output

#python.exe "C:\Users\ASUS\Documents\Python Scripts\onlab2\dash_test.py"


df = pd.read_csv("https://raw.githubusercontent.com/laszlogabor/onlab2/master/main_teams_meas.csv")



mgr_options = df["query"].unique()

app = dash.Dash()

app.layout = html.Div([
    html.H2("Social media - Football teams by followers"),
    html.Div(
        [
            dcc.Dropdown(
                id="team",
                options=[{
                    'label': i,
                    'value': i
                } for i in mgr_options],
                value='Choose a team!'),
        ],a
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Div(
        [
            dcc.Dropdown(
                id="team_res",
                options=[{
                    'label': i,
                    'value': i
                } for i in mgr_options],
                value='Choose a team!'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(
        id='funnel-graph',
        figure={
            'layout': {
                'width': '40%'
            }
        }
    ),        
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'width': '25%',
                'display': 'inline-block'
            }
        }
    )
])


@app.callback(
    Output('funnel-graph', 'figure'),
    [Input('team', 'value'), Input('team_res', 'value')])
def update_graph(Team, Team_res):
    df_plot = df[df['query'] == Team]

    trace1 = go.Bar(x=df_plot['query'], y=df_plot['facebook_likes'], name='Facebook',  marker=dict(color=('rgb(59, 89, 152)')))
    trace2 = go.Bar(x=df_plot['query'], y=df_plot['twitter_followers'], name='Twitter', marker=dict(color=('rgb(29, 161, 242)')))
    trace3 = go.Bar(x=df_plot['query'], y=df_plot['instagram_followers'], name='Instagram', marker=dict(color=('rgb(193, 53, 132)')))

    return {
        'data': [trace1, trace2, trace3],
        'layout':
        go.Layout(
            title='Follower counts for {}'.format(Team)
        )
    }




if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1', port=801)