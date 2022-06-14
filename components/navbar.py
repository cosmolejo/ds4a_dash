import dash
import dash_bootstrap_components as dbc
from dash import html
from components.styles import *
from dash.dependencies import Input, Output, State

navbar = dbc.NavbarSimple(
    children=[
        dbc.Button(
            outline=True,
            color="secondary",
            className="navbar-toggler-icon",
            id="btn_sidebar",
        ),
    ],
    brand="DS4A",
    brand_href="#",
    color="dark",
    dark=True,
    fluid=True,
)