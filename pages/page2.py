from dash import dcc, html, Input, Output, callback
import pandas as pd
import numpy as np
import plotly.express as px

from components.app import app



df_heatmap_barranquilla = pd.read_csv("data/local/df_heatmap_barranquilla.csv")
df_heatmap_envigado = pd.read_csv("data/local/df_heatmap_envigado.csv")
df_heatmap_palmira = pd.read_csv("data/local/df_heatmap_palmira.csv")
df_heatmap_medellin = pd.read_csv("data/local/df_heatmap_medellin.csv")

accidentes_por_year = pd.read_csv("data/local/accidentes_por_year.csv")
accidentes_por_mes = pd.read_csv("data/local/accidentes_por_mes.csv")
accidentes_por_dia = pd.read_csv("data/local/accidentes_por_dia.csv")
accidentes_hora = pd.read_csv("data/local/accidentes_hora.csv")


envigado_heat = px.density_mapbox(df_heatmap_envigado, lat='LAT', lon='LON', z='Cuenta', radius=10,
                        center=dict(lat=6.17, lon=-75.58), zoom=13,
                        mapbox_style="stamen-terrain")

envigado_heat.update_layout(title="Envigado accident heatmap", paper_bgcolor="#F8F9F9")
medellin_heat = px.density_mapbox(df_heatmap_medellin, lat='LAT', lon='LON', z='Cuenta', radius=10,
                        center=dict(lat=6.25, lon=-75.60), zoom=11,
                        mapbox_style="stamen-terrain")
medellin_heat.update_layout(title="Medellín accident heatmap", paper_bgcolor="#F8F9F9")


layout = html.Div([
#     html.H3('Page 2'),
#    html.P('here goes the local plots')
html.Div(
    [
        # Place the main graph component here:
        dcc.Graph(figure=envigado_heat, id="env_heat")
    ]),
    html.Div(
    [
        # Place the main graph component here:
        dcc.Graph(figure=medellin_heat, id="med_heat")
    ])
])

