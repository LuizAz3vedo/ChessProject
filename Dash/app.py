import dash 
import dash_bootstrap_components as dbc

# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY, dbc.icons.BOOTSTRAP], suppress_callback_exceptions=True)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH,  dbc.icons.FONT_AWESOME], suppress_callback_exceptions=True)

app.scripts.config.serve_locally = True
server = app.server