import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from components.styles import *
from dash.dependencies import Input, Output, State



navbar = dbc.NavbarSimple(
    children=[
         dbc.Nav(
            [
                dbc.NavLink(
                    "National overview",
                    href="/page-1",
                    active="exact",
                    id="page-1-link",
                ),
                dbc.NavLink(
                    "Local overview", href="/page-2", active="exact", id="page-2-link"
                ),
                dbc.NavLink(
                    "Clusters", href="/page-3", active="exact", id="page-3-link"
                ),
                dbc.NavLink(
                    "Accidents prediction",
                    href="/page-4",
                    active="exact",
                    id="page-4-link",
                ),
                
            ],
            vertical=False,
            pills=True,
        ),
        
        dbc.Button(
            "☰ Filters",
            outline=False,
            color="secondary",
            className="me-1",
            id="btn_sidebar",
        ),
    ],
    brand="DS4A",
    brand_href="/",
    color="dark",
    dark=True,
    fluid=True,
)


def navbar_callbacks(app):
   pass