from datetime import date
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px

from components.app import app
import dash_bootstrap_components as dbc

from components.styles import *

df_mes_dow = pd.read_csv('data/Clusterizada.csv')
df_mes_dow['Cluster'] = df_mes_dow['Cluster'].astype(str)

lugar = 'Todo'

if lugar != 'Todo':
    base = df_mes_dow.loc[df_mes_dow['Ciudad'] == lugar, ]
else:
    base = df_mes_dow


cluster = px.scatter(base,
                     x="Heridos", y="Muertos",
                     hover_data=["Ciudad", "Heridos", "Muertos", "Cluster"],
                     color='Cluster', title='Clusters by DOW and month')


layout = dbc.Container([
    dcc.Store(id='memory-output'),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=cluster, id="cluster")


        ], width={'size': 12, 'offset': 0},
            style={"height": "100%"},)

    ])
], style={"height": "100%"},)


##############################################################################
# Cities Picker
##############################################################################


drop = dcc.Dropdown(
    options=[{"label": i, "value": i} for i in df_mes_dow.Ciudad.unique()],
    value=[],
    id='city_dropdown',
    multi=True)

sidebar = html.Div(
    [
        html.Img(src="assets/img/LOGO.png", width="200px",
                 style={'textAlign': 'center'}),
        html.Hr(),
        html.H5("Select cities"),
        drop


    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)


def page3_callbacks(app):
    @app.callback(Output("cluster", "figure"),
                  Input("city_dropdown", "value"),)
    def filter_clusters(city_dropdown):
        if not city_dropdown:
            # Return all the rows on initial load/no country selected.
            lugar = 'Todo'
            base = df_mes_dow
        else:
            lugar = city_dropdown
            base = df_mes_dow.query('Ciudad in @city_dropdown')
        cluster = px.scatter(base,
                             x="Heridos", y="Muertos",
                             hover_data=["Ciudad", "Heridos",
                                         "Muertos", "Cluster"],
                             color='Cluster', title='Clusters by DOW and month')

        return cluster
