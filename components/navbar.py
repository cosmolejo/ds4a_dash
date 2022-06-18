import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from components.styles import *
from dash.dependencies import Input, Output, State
from datetime import date


navbar = dbc.NavbarSimple(
    children=[
        dcc.DatePickerRange(
            id="my-date-picker-range",
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2017, 9, 19),
            initial_visible_month=date(2017, 8, 5),
            end_date=date(2017, 8, 25),
        ),
        dbc.Button(
            outline=True,
            color="secondary",
            className="navbar-toggler-icon",
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
    @app.callback(
        Output("output-container-date-picker-range", "children"),
        Input("my-date-picker-range", "start_date"),
        Input("my-date-picker-range", "end_date"),
    )
    def update_output(start_date, end_date):
        string_prefix = "You have selected: "
        if start_date is not None:
            start_date_object = date.fromisoformat(start_date)
            start_date_string = start_date_object.strftime("%B %d, %Y")
            string_prefix = string_prefix + "Start Date: " + start_date_string + " | "
        if end_date is not None:
            end_date_object = date.fromisoformat(end_date)
            end_date_string = end_date_object.strftime("%B %d, %Y")
            string_prefix = string_prefix + "End Date: " + end_date_string
        if len(string_prefix) == len("You have selected: "):
            return "Select a date to see it displayed here"
        else:
            return string_prefix