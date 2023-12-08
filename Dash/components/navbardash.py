import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, Dash

from app import *

giturl = 'https://github.com/LuizAz3vedo'
chessurl = 'https://www.chess.com'


header = dbc.NavbarSimple(
    children=[
        dbc.NavItem(html.Img(src="caminho_para_a_foto.jpg", height="30px"), style={'margin-right': '1rem'}),
        dbc.NavItem([html.P("Luiz Azevedo", className="nav-icon-text"), html.I(className="fa-solid fa-chess", style={'margin-left': '0.5rem'})], style={'display': 'flex', 'align-items': 'center'}),

    ],
    brand=dbc.NavItem([html.I(className="fa-solid fa-chess", style={'margin-right': '0.5rem'}), html.P("Chess", className="nav-icon-text")], style={'display': 'flex', 'align-items': 'center'}),
    brand_href=chessurl,
    color="primary",
    dark=True,
)
