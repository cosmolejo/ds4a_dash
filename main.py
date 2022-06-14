from pickle import TRUE
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from components.styles import *
from components.sidebar import *
from components.navbar import *

from pages import index,page1, page2,page3,page4,not_found


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], 
suppress_callback_exceptions=True, 
title='ds4a')

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


content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div(
    [dcc.Store(id="side_click"),
    dcc.Location(id="url"), 
    navbar, 
    sidebar, 
    content,
    ],
)


# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to tell see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 4)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 4)]


@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
    )
def render_page_content(pathname):
    if pathname in ["/"]:
        return index.layout
    elif pathname == "/page-1":
        return page1.layout
    elif pathname == "/page-2":
        return page2.layout
    elif pathname == "/page-3":
        return page3.layout
    elif pathname == "/page-4":
        return page4.layout
    # If the user tries to reach a different page, return a 404 message
    return not_found.layout


if __name__ == "__main__":
    app.run_server(debug=True, port=8086)
