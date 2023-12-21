import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, Dash

from app import *

giturl = 'https://github.com/LuizAz3vedo'
chessurl = 'https://www.chess.com'


header = dbc.NavbarSimple(
    children=[
        dbc.NavItem(html.Img(src="../assets/canva1.jpg", height="39px", width = "39px", style={'border-radius': '100%'}), style={'margin-right': '1rem'}),
        dbc.NavItem([html.P("Luiz Azevedo", className="nav-icon-text"), html.A(html.I(className="fa-brands fa-github", style={'margin-left': '0.5rem', 'color':'white', 'font-size': '1.3rem'}), href=giturl)], style={'display': 'flex', 'align-items': 'center'}),
    ],
    brand=dbc.NavItem(html.I(className="fa-solid fa-chess", style={'margin-right': '1rem', 'cursor': 'pointer', 'height': '30px', 'font-size': '1.3rem'}), className="nav-icon-text"),
    brand_href=chessurl,
    color="primary",
    dark=True,
    style={'height': '70px'}  # Increase the height of the navbar
)

