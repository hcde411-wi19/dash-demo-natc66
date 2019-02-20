# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

#data from survey about women in gaming
#configuration 1 that focuses on the different types of sexism
categories = ['Harassment because of gender', 'Microaggressions', 'Online Toxicity', 'Stigma of Women in Gaming', 'Unwanted Sexual Advances']

most_experienced_in_community = [2, 11, 14, 6, 7]
somewhat_experienced_in_community = [6, 7, 8, 11, 4]
neutral_experienced_in_community = [9, 8, 5, 11, 8]
somewhat_NOTexperienced_in_community = [9, 9, 5, 11, 5]
least_experienced_in_community = [12, 6, 5, 2, 17]

#configuration 2 that focuses on the experience level
categories2 = ['most experienced', 'somewhat experienced', 'neutral', 'somewhat not experienced', 'least experienced']
harassment = [2, 6, 9, 9, 12]
micro = [11, 7, 8, 9, 6]
online = [14, 8, 5, 5, 5]
stigma = [6, 11, 11, 11, 2]
sexual = [7, 4, 8, 5, 17]
none = [7, 11, 6, 8, 5]


app = dash.Dash(__name__, static_folder='static')
app.layout = html.Div(children=[

    # set the page heading
    html.H1(children='Scatter Plot'),

    # set the description underneath the heading
    html.Div(children='''
        A bar chart showing how women feel about sexism in the gaming community
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='',
        figure={
            'data': [
            	# Alternative layout with the category of sexism on the x axis
#                {'x': categories, 'y':most_experienced_in_community, 'type': 'bar', 'name': 'most experienced'},
#                {'x': categories, 'y':somewhat_experienced_in_community, 'type': 'bar', 'name': 'somewhat experienced'},
#                {'x': categories, 'y':neutral_experienced_in_community, 'type': 'bar', 'name': 'neutral'},
#                {'x': categories, 'y':somewhat_NOTexperienced_in_community, 'type': 'bar', 'name': 'somewhat not experienced'},
#                {'x': categories, 'y':least_experienced_in_community, 'type': 'bar', 'name': 'least experienced'},

                {'x': categories2, 'y':harassment, 'type': 'bar', 'name': 'Harassment because of Gender'},
                {'x': categories2, 'y':micro, 'type': 'bar', 'name': 'Microaggressions'},
                {'x': categories2, 'y':online, 'type': 'bar', 'name': 'Online Toxicity'},
                {'x': categories2, 'y':stigma, 'type': 'bar', 'name': 'Stigma of Women in Gaming'},
                {'x': categories2, 'y':sexual, 'type': 'bar', 'name': 'Unwanted Sexual Advances'},
                {'x': categories2, 'y':none , 'type': 'bar', 'name': 'Declined to Answer'},

            ],

            'layout': {
                'title': 'Sexism in Gaming',
                
                #axis labels
                'xaxis': {'title': 'Experience within the Gaming Community'},
                'yaxis': {'title': 'Number of People'},
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
