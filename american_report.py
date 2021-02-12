# Author: Skander Marnissi 

import pandas as pd
import numpy as np
import seaborn as sns
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import plotly.express as px
import plotly
from dash.dependencies import Input, Output, State
america = pd.read_csv("./dataset/Bank_of_America_data.csv")
america["ID"] = list(america.index)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    
    html.H1([
        'American Bank Dashboard'
    ], style = {
        'font-family': 'cursive',
        'text-align': 'center',
        'color': '#010169',
        'font-style': 'oblique'
    }),
    
    html.Div([   
        # CountPlot BAD Variable
        dcc.Graph(
            id='count/bad',
            figure={
            'data': [
                {
                    'x': ["Bad : Yes", "Bad : No"], 
                    'y': [america.where(america['BAD'] == 1)['ID'].count(), america.where(america['BAD'] == 0)['ID'].count()], 
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#F7C5BA', '#DB93A6']
                    }
                }
            ],
                
            'layout': {
                'title': 'Distribution of target variable',
                'width': "508", 
                'height': "600"
            }    
        }
        ),
    
        # CountPlot REASON
        dcc.Graph(
            id='count/reason',
            figure={
                'data': [
                    {'x': ["HomeImp", "DebtCon"], 
                    'y': [america.where(america['REASON'] == "HomeImp")['ID'].count(), america.where(america['REASON'] == "DebtCon")['ID'].count()], 
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#92A0FF', '#F2CCC4']
                    }
            }
                ],
                'layout': {
                    'title': 'Reason of debt Distribution',
                    'width': "508", 
                    'height': "600"
                }
            }
        ),

        # CountPlot LOAN
        dcc.Graph(
            id='count/loan',
            figure={
                'data': [
                    {'x': ["5000 ~ 10000", "10000 ~ 12500", "12500 ~ 15000", "15000 ~ 17500", "17500 ~ 20000", "20000 ~ 21000"], 
                    'y': [ america.where((america['LOAN'] >= 5000) & (america['LOAN'] < 10000) )['ID'].count(),
                            america.where((america['LOAN'] >= 10000) & (america['LOAN'] < 12500) )['ID'].count(),
                            america.where((america['LOAN'] >= 12500) & (america['LOAN'] < 15000) )['ID'].count(), 
                            america.where((america['LOAN'] >= 15000) & (america['LOAN'] < 17500) )['ID'].count(), 
                            america.where((america['LOAN'] >= 20000) & (america['LOAN'] < 21000) )['ID'].count(),
                            america.where((america['LOAN'] >= 21000) & (america['LOAN'] < 500000) )['ID'].count()
                    ],
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#F2CDC4', '#D69CAC', '#AA87E6', '#92A0FF', '#85CFFA', '#E6B0FA']
                    }
            }
                ],
                'layout': {
                    'title': 'Loan Distribution',
                    'width': "600", 
                    'height': "600"
                }
            }
        ),

        # CountPlot JOB
        dcc.Graph(
            id='count/job',
            figure={
                'data': [
                    {'x': ['Other', 'Office', 'Sales', 'Mgr', 'ProfExe', 'Self'], 
                    'y': [america.where(america['JOB'] == 'Office')['ID'].count(),
                        america.where(america['JOB'] == 'Sales')['ID'].count(),
                        america.where(america['JOB'] == 'Mgr')['ID'].count(),
                        america.where(america['JOB'] == 'ProfExe')['ID'].count(),
                          america.where(america['JOB'] == 'Self')['ID'].count(),
                          america.where(america['JOB'] == 'Other')['ID'].count()
                        ], 
                    
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#CFA2E8', '#F8B3FF', '#B3C0FF', '#D7BFFF', '#85CFFA', '#D69CAC']
                    }
            }
                ],
                'layout': {
                    'title': 'Job Distribution',
                    'width': "600", 
                    'height': "600"
                }
            }
        ),
        
        # CountPlot DEROG 
        dcc.Graph(
            id='count/derog',
            figure={
                'data': [
                    {'x': [ "0", "3", "2", "1", "4", "5",  "6",  "7",  "8",  "9", "10"], 
                    'y': [america.where(america['DEROG'] == 1)['ID'].count(), 
                        america.where(america['DEROG'] == 2)['ID'].count(),
                        america.where(america['DEROG'] == 3)['ID'].count(),
                          america.where(america['DEROG'] == 4)['ID'].count(),
                          america.where(america['DEROG'] == 5)['ID'].count(),
                          america.where(america['DEROG'] == 6)['ID'].count(),
                          america.where(america['DEROG'] == 7)['ID'].count(),
                          america.where(america['DEROG'] == 8)['ID'].count(),
                          america.where(america['DEROG'] == 9)['ID'].count(),
                          america.where(america['DEROG'] == 10)['ID'].count(),
                        ], 
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#C6EBED', '#EDAFB3', '#9ABFE6', '#CFA2E8', '#F8B3FF', '#B3C0FF', '#D7BFFF', '#85CFFA', '#D69CAC', '#F2CCC4' ]
                    }
            }
                ],
                'layout': {
                    'title': 'Derog Distribution',
                    'width': "508", 
                    'height': "600"
                }
            }
        ),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=False, port = 3006)
