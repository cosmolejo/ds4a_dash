from dash import dcc, html, Input, Output, callback
from components.navbar import *
from components.app import app

navbar_callbacks(app)
layout = html.Div([
    html.H3('Landing page'),
    html.P('this is the index'),
    html.Div(id="output-container-date-picker-range")
])

