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

taiwan = pd.read_excel("./dataset/default-of-credit-card-clients.xls", header = 1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.P([
        ''
    ], id = 'tmp'),
    
    html.H1([
        'Taiwanese Bank Dashboard'
    ], style = {
        'font-family': 'cursive',
        'text-align': 'center',
        'color': '#010169',
        'font-style': 'oblique'
    }),
    
    html.Div([
        
        
       
        # CountPlot Target Variable
        dcc.Graph(
            id='count/defpay',
            figure={
                'data': [
                    {'x': ["Yes", "No"], 
                    'y': [taiwan.where(taiwan['default payment next month'] == 1)['ID'].count(), taiwan.where(taiwan['default payment next month'] == 0)['ID'].count()], 
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
    
        # CountPlot Sex
        dcc.Graph(
            id='count/sex',
            figure={
                'data': [
                    {'x': ["Male", "Female"], 
                    'y': [taiwan.where(taiwan['SEX'] == 1)['ID'].count(), taiwan.where(taiwan['SEX'] == 2)['ID'].count()], 
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#92A0FF', '#F2CCC4']
                    }
            }
                ],
                'layout': {
                    'title': 'Sex Distribution',
                    'width': "508", 
                    'height': "600"
                }
            }
        ),

        # CountPlot Age
        dcc.Graph(
            id='count/age',
            figure={
                'data': [
                    {'x': ["20 ~ 30", "30 ~ 40", "40 ~ 50", "50 ~ 60", "60 ~ 70", "70 ~ 80"], 
                    'y': [ taiwan.where((taiwan['AGE'] >= 20) & (taiwan['AGE'] < 30) )['ID'].count(),
                            taiwan.where((taiwan['AGE'] >= 30) & (taiwan['AGE'] < 40) )['ID'].count(),
                            taiwan.where((taiwan['AGE'] >= 40) & (taiwan['AGE'] < 50) )['ID'].count(), 
                            taiwan.where((taiwan['AGE'] >= 50) & (taiwan['AGE'] < 60) )['ID'].count(), 
                            taiwan.where((taiwan['AGE'] >= 60) & (taiwan['AGE'] < 70) )['ID'].count(),
                            taiwan.where((taiwan['AGE'] >= 70) & (taiwan['AGE'] < 80) )['ID'].count()
                    ],
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#F2CDC4', '#D69CAC', '#AA87E6', '#92A0FF', '#85CFFA', '#E6B0FA']
                    }
            }
                ],
                'layout': {
                    'title': 'Age Distribution',
                    'width': "600", 
                    'height': "600"
                }
            }
        ),

        # CountPlot Education
        dcc.Graph(
            id='count/education',
            figure={
                'data': [
                    {'x': ["Graduate School", "University", "High School", "Others"], 
                    'y': [taiwan.where(taiwan['EDUCATION'] == 1)['ID'].count(),
                        taiwan.where(taiwan['EDUCATION'] == 2)['ID'].count(),
                        taiwan.where(taiwan['EDUCATION'] == 3)['ID'].count(),
                        taiwan.where((taiwan['EDUCATION'] >= 4) | (taiwan['EDUCATION'] == 0) )['ID'].count()
                        ], 
                    
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#CFA2E8', '#F8B3FF', '#B3C0FF', '#D7BFFF']
                    }
            }
                ],
                'layout': {
                    'title': 'Education Distribution',
                    'width': "600", 
                    'height': "600"
                }
            }
        ),
        
        # CountPlot Marriage 
        dcc.Graph(
            id='count/marriage',
            figure={
                'data': [
                    {'x': ["Single", "Married", "Others"], 
                    'y': [taiwan.where(taiwan['MARRIAGE'] == 1)['ID'].count(), 
                        taiwan.where(taiwan['MARRIAGE'] == 2)['ID'].count(),
                        taiwan.where(taiwan['MARRIAGE'] == 3)['ID'].count(),
                        ], 
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#C6EBED', '#EDAFB3', '#9ABFE6']
                    }
            }
                ],
                'layout': {
                    'title': 'Marriage Distribution',
                    'width': "508", 
                    'height': "600"
                }
            }
        ),
    ]),
    
    html.Div([
        
        # LIMIT_BAL / SEX
        dcc.Graph(
            id='sex/limit_bal',
            figure={
                'data': [
                    {'x': ["Homme", "Femme"], 
                    'y': [taiwan.where(taiwan['SEX'] == 1)['LIMIT_BAL'].mean(), taiwan.where(taiwan['SEX'] == 2)['LIMIT_BAL'].mean()], 
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#92A0FF', '#F2CCC4']
                    }
            }
                ],
                'layout': {
                    'title': 'Credit Amount by gender',
                    'width': "508", 
                    'height': "600"
                }
            }
        ),

        # LIMIT_BAL / EDUCATION
        dcc.Graph(
            id='Limit_bal/education',
            figure={
                'data': [
                    {'x': ["Graduate School", "University", "High School", "Others"], 
                    'y': [taiwan.where(taiwan['EDUCATION'] == 1)['LIMIT_BAL'].mean(), 
                        taiwan.where(taiwan['EDUCATION'] == 2)['LIMIT_BAL'].mean(),
                        taiwan.where(taiwan['EDUCATION'] == 3)['LIMIT_BAL'].mean(),
                        taiwan.where((taiwan['EDUCATION'] >= 4) | (taiwan['EDUCATION'] == 0))['LIMIT_BAL'].mean()
                        ],
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#CFA2E8', '#F8B3FF', '#B3C0FF', '#D7BFFF']
                    }
                    }
                ],
                'layout': {
                    'title': 'Credit amout by educational level',
                    'width': "600", 
                    'height': "600"
                }
            }
        ),
        
        # LIMIT_BAL / Target Variable
        dcc.Graph(
            id='Limit_bal/Default payment next month',
            figure={
                'data': [
                    {'x': ["Yes", "No"], 
                    'y': [taiwan.where(taiwan['default payment next month'] == 1)['LIMIT_BAL'].mean(), 
                        taiwan.where(taiwan['default payment next month'] == 0)['LIMIT_BAL'].mean()

                        ], 
                    'type': 'bar', 
                    'name': 'SF',
                    'marker': {
                        'color': ['#F7C5BA', '#DB93A6']
                    }
            }
                ],
                'layout': {
                    'title': 'Credit amout by clients classes',
                    'width': "508", 
                    'height': "600"
                }
            }
        ),
    ])   
])







if __name__ == '__main__':
    app.run_server(debug=True, port = 3004)