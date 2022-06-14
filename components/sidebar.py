import dash
import dash_bootstrap_components as dbc
from dash import html
from components.styles import *
from dash.dependencies import Input, Output, State

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


sidebar = html.Div(
    [
        html.Img(src = 'assets/img/ds4a.jpg', width="200px"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("National overview", href="/page-1", active='exact', id="page-1-link"),
                dbc.NavLink("Local overview", href="/page-2",  active='exact', id="page-2-link"),
                dbc.NavLink("Clusters", href="/page-3",  active='exact', id="page-3-link"),
                dbc.NavLink("Accidents prediction", href="/page-4",  active='exact', id="page-4-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)


@app.callback(
    [
        Output("sidebar", "style"),
        Output("page-content", "style"),
        Output("side_click", "data"),
    ],

    [Input("btn_sidebar", "n_clicks")],
    [
        State("side_click", "data"),
    ]
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
        cur_nclick = 'SHOW'

    return sidebar_style, content_style, cur_nclick