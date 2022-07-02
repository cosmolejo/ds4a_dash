import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from components.styles import *
from dash.dependencies import Input, Output, State
from datetime import date

from components.app import app





##############################################################################
# Date Picker
##############################################################################
date_picker = dcc.DatePickerRange(
            id="my-date-picker-range",
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2017, 9, 19),
            initial_visible_month=date(2017, 8, 5),
            end_date=date(2017, 8, 25),
            style=DATE_PICKER_STYLE,
        )






sidebar = html.Div(
    [
        html.Img(src="assets/img/ds4a.jpg", width="200px"),
        html.Hr(),
         html.H5("Select dates"),
        date_picker,
        
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)


def sidebar_callbacks(app):
    @app.callback(
        [
            Output("sidebar", "style"),
            Output("page-content", "style"),
            Output("side_click", "data"),
        ],
        [Input("btn_sidebar", "n_clicks")],
        [State("side_click", "data"),],
    )
    def toggle_sidebar(n, nclick):
        if n:
            if nclick == "SHOW":
                sidebar_style = SIDEBAR_HIDEN
                content_style = CONTENT_STYLE1
                cur_nclick = "HIDDEN"
            else:
                sidebar_style = SIDEBAR_STYLE
                content_style = CONTENT_STYLE
                cur_nclick = "SHOW"
        else:
            sidebar_style = SIDEBAR_STYLE
            content_style = CONTENT_STYLE
            cur_nclick = "SHOW"

        return sidebar_style, content_style, cur_nclick
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

   
