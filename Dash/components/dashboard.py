from __future__ import division 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, Dash
from pandas._libs import properties

from app import *
from components import navbardash

# ↧ layout ↧ ========================================================================================
layout = dbc.Container(fluid=True, children=[
    dbc.Row([
        dbc.Col([
            navbardash.header
        ], style={'padding': '0'})
    ]),
])

    

