import dash
import dash_bootstrap_components as dbc

external_style = ['https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css']

app = dash.Dash( external_stylesheets=[dbc.themes.SUPERHERO, external_style], 
suppress_callback_exceptions=True,
title='ds4a')
