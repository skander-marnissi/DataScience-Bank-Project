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
import base64


german = pd.read_csv("./dataset/DataFrameGermanDecodee.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    
    html.H1([
        'German Bank Dashboard'
    ], style = {
        'font-family': 'cursive',
        'text-align': 'center',
        'color': '#010169',
        'font-style': 'oblique'
    }),
    
   
    html.Div([    
        
        # Distribution de la variable cible Risk
        dcc.Graph(
            id='G1',
            figure={
                'data': [
                    {
                        'x': ["Bad Risk", "Good Risk"], 
                        'y': [german.where(german['Risk'] == 0).iloc[:, 0].count(),
                              german.where(german['Risk'] == 1).iloc[:, 0].count()],
                        'type': 'bar', 
                        'name': 'SF',
                        'marker': {
                            'color': ['#F7C5BA', '#DB93A6']
                        }
                    }
                ],

                'layout': {
                    'title': 'Distribution de la  variable cible Risk',
                    'width': "550", 
                    'height': "450"
                }    
            }
        ),
        
        # Distribution de la variable Job en fonction de notre variable cible Risk
        dcc.Graph(
            id='G2',
            figure={
                'data': [
                    {
                        'x': ["unemployed/ unskilled  - non-resident", "unskilled - resident", "skilled employee / official", "management/ self-employed/highly qualified employee/ officer"], 
                        'y': [german.where(german['Job'] == "unemployed/ unskilled  - non-resident")['Risk'].mean(),
                              german.where(german['Job'] == "unskilled - resident")['Risk'].mean(),
                              german.where(german['Job'] == "skilled employee / official")['Risk'].mean(),
                              german.where(german['Job'] == "management/ self-employed/highly qualified employee/ officer")['Risk'].mean()],
                        'type': 'bar', 
                        'name': 'SF',
                        'marker': {
                            'color': ['#F7C5BA', '#DB93A6', '#D6EDCE', '#D6C8A9']
                        }
                    }
                ],

                'layout': {
                    'title': 'Distribution de la variable Job en fonction de notre variable cible Risk',
                    'width': "1150", 
                    'height': "450"
                }    
            }
        ),
        
        # Distribution des individus en fonction de Personal status and sex et Credit amount
        dcc.Graph(
            id='G3',
            figure={
                'data': [
                {'x': ["unemployed/ unskilled  - non-resident", "unskilled - resident", "skilled employee / official", "management/ self-employed/highly qualified employee/ officer"],
                 'y': [german.where((german['Job'] == "unemployed/ unskilled  - non-resident") & (german['Personal status and sex'] == "male:divorced/separated"))['Credit amount'].mean(),
                       german.where((german['Job'] == "unskilled - resident") & (german['Personal status and sex'] == "male:divorced/separated"))['Credit amount'].mean(),
                       german.where((german['Job'] == "skilled employee / official") & (german['Personal status and sex'] == "male:divorced/separated"))['Credit amount'].mean(),
                       german.where((german['Job'] == "management/ self-employed/highly qualified employee/ officer") & (german['Personal status and sex'] == "male:divorced/separated"))['Credit amount'].mean()],
                 'type': 'bar', 'name': 'male:divorced/separated'},
                {'x': ["unemployed/ unskilled  - non-resident", "unskilled - resident", "skilled employee / official", "management/ self-employed/highly qualified employee/ officer"],
                 'y': [german.where((german['Job'] == "unemployed/ unskilled  - non-resident") & (german['Personal status and sex'] == "female:divorced/separated/married"))['Credit amount'].mean(),
                       german.where((german['Job'] == "unskilled - resident") & (german['Personal status and sex'] == "female:divorced/separated/married"))['Credit amount'].mean(),
                       german.where((german['Job'] == "skilled employee / official") & (german['Personal status and sex'] == "female:divorced/separated/married"))['Credit amount'].mean(),
                       german.where((german['Job'] == "management/ self-employed/highly qualified employee/ officer") & (german['Personal status and sex'] == "female:divorced/separated/married"))['Credit amount'].mean()],
                 'type': 'bar', 'name': 'female:divorced/separated/married'},
                {'x': ["unemployed/ unskilled  - non-resident", "unskilled - resident", "skilled employee / official", "management/ self-employed/highly qualified employee/ officer"],
                 'y': [german.where((german['Job'] == "unemployed/ unskilled  - non-resident") & (german['Personal status and sex'] == "male:single"))['Credit amount'].mean(),
                       german.where((german['Job'] == "unskilled - resident") & (german['Personal status and sex'] == "male:single"))['Credit amount'].mean(),
                       german.where((german['Job'] == "skilled employee / official") & (german['Personal status and sex'] == "male:single"))['Credit amount'].mean(),
                       german.where((german['Job'] == "management/ self-employed/highly qualified employee/ officer") & (german['Personal status and sex'] == "male:single"))['Credit amount'].mean()],
                 'type': 'bar', 'name': 'male:single'},
                {'x': ["unemployed/ unskilled  - non-resident", "unskilled - resident", "skilled employee / official", "management/ self-employed/highly qualified employee/ officer"],
                 'y': [german.where((german['Job'] == "unemployed/ unskilled  - non-resident") & (german['Personal status and sex'] == "male:married/widowed"))['Credit amount'].mean(),
                       german.where((german['Job'] == "unskilled - resident") & (german['Personal status and sex'] == "male:married/widowed"))['Credit amount'].mean(),
                       german.where((german['Job'] == "skilled employee / official") & (german['Personal status and sex'] == "male:married/widowed"))['Credit amount'].mean(),
                       german.where((german['Job'] == "management/ self-employed/highly qualified employee/ officer") & (german['Personal status and sex'] == "male:married/widowed"))['Credit amount'].mean()],
                 'type': 'bar', 'name': 'male:married/widowed'}
                
            ],

                'layout': {
                    'title': 'Distribution des individus en fonction de Personal status and sex et Credit amount',
                    'width': "1350", 
                    'height': "450"
                }    
            }
        ),
        
        # Distribution des individus par Age in years en fonction de Credit amount
        dcc.Graph(
            id='G4',
            figure={
                'data': [
                    {
                        'x': ["19 ~ 29", "30 ~ 39", "40 ~ 49", "50 ~ 59", "60 ~ 69","70 ~ 86"], 
                        'y': [german.where((german['Age in years'] >= 19) & (german['Age in years'] < 29) )['Credit amount'].mean(),
                            german.where((german['Age in years'] >= 30) & (german['Age in years'] < 39) )['Credit amount'].mean(), 
                            german.where((german['Age in years'] >= 40) & (german['Age in years'] < 49) )['Credit amount'].mean(),
                            german.where((german['Age in years'] >= 50) & (german['Age in years'] < 59) )['Credit amount'].mean(),
                            german.where((german['Age in years'] >= 60) & (german['Age in years'] < 69) )['Credit amount'].mean(),
                            german.where((german['Age in years'] >= 70) & (german['Age in years'] < 76) )['Credit amount'].mean()
                        ],
                        'type': 'bar', 
                        'name': 'SF',
                        'marker': {
                            'color': ['#F7C5BA', '#DB93A6', '#A399BF', '#E49BF0', '#D6EDCE', '#D6C8A9']
                        }
                    }
                ],

                'layout': {
                    'title': 'Distribution de la variable Job en fonction de notre variable cible Risk',
                    'width': "1150", 
                    'height': "450"
                }    
            }
        )
])
    ])


if __name__ == '__main__':
    app.run_server(debug=False, port = 3005)