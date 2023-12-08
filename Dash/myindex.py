import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, Dash

from app import *
# Import the components module from the same directory
from components import dashboard
#============ Layout  ====================#

# Layout da página de dashboard com barra lateral específica
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

# Mapeia as URLs para os layouts correspondentes
page_layouts = {
    '/dashboard': layout_dashboard
}

app.layout = html.Div([
    dcc.Location(id='url'),
    # Conteúdo da página selecionada
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    # Retorna o layout correspondente à URL atual
    return page_layouts.get(pathname, page_layouts['/dashboard'])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port='8081', debug=True)