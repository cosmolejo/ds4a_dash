import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.SUPERHERO], 
suppress_callback_exceptions=True, 
title='ds4a')
