from dash import dcc, html, Input, Output, callback 
import dash_bootstrap_components as dbc

layout = html.Div(dbc.Container(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.Div(id = 'page-2-display-value'),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",)


@callback(
    Output('page-2-display-value', 'children'),
    [Input('url', 'pathname')])
def callback_func(pathname):
    return f"The pathname {pathname} was not recognised..."