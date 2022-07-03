from pickle import TRUE
from pkgutil import get_data
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from components.styles import *
from components.sidebar import *
from components.navbar import *
from data.datasets import Datasets


from components.app import app

from pages import index, page1, page2, page3, page4, not_found


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],
                suppress_callback_exceptions=True,
                title='ds4a')

sidebar_callbacks(app)
navbar_callbacks(app)
page1.page1_callbacks(app)


content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div(
    [dcc.Store(id="side_click"),
     dcc.Location(id="url"),
     navbar,
     content,
     sidebar,

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
        return False, False, False
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

  
    app.run_server(debug=True, port=8086 )
