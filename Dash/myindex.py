import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, Dash

from app import *

from components import dashboard
#============ Layout  ====================#

layout_dashboard = dbc.Container(fluid=True, style={'padding': '0'})

row_style = {'margin': '0', 'width': '100%'}
col_style = {'padding': '0'}

layout_dashboard.children = [
    dbc.Row([
        dbc.Col([   
            dashboard.layout
        ], sm=12, lg=12, style=col_style)
    ], style=row_style)
]

page_layouts = {
    '/dashboard': layout_dashboard
}

app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    return page_layouts.get(pathname, page_layouts['/dashboard'])

if __name__ == '__main__':
    app.run_server(port='8084', debug=True)