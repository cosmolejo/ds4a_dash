from dash import dcc, html, Input, Output, callback
from components.app import app
import pandas as pd
import geopandas

import plotly.graph_objects as go
import plotly.express as px
import pyproj
import json


##################################################
# Data preparation
#################################################


map_df = geopandas.read_file('data/nacional/accidentes.geojson')
accidentes_por_year = pd.read_csv("data/nacional/accidentes_por_year.csv")
accidentes_total = pd.read_csv("data/nacional/accidentes_total.csv")
accidentes_por_dia = pd.read_csv("data/nacional/accidentes_por_dia.csv")
accidentes_por_dia_completo = pd.read_csv(
    "data/nacional/accidentes_por_dia_completo.csv")


Map_Fig = px.choropleth(map_df, geojson=map_df.geometry,
                        locations=map_df.index, color="Accidentes")
Map_Fig.update_geos(fitbounds="locations", visible=True)
Map_Fig.update_layout(title="National highway's accidents",
                      paper_bgcolor="#F8F9F9")


Map_Fig_norm = px.choropleth(map_df, geojson=map_df.geometry,
                             locations=map_df.index, color="AccidentesNormalizado")
Map_Fig_norm.update_geos(fitbounds="locations", visible=True)
Map_Fig_norm.update_layout(title="Normalized National highway's accidents",
                           paper_bgcolor="#F8F9F9")

bar_plot_nal = px.bar(accidentes_total, x="Departamento", y="AccidentesNormalizado",
                      title="Accidentes por millón de habitantes", barmode='group')
bar_plot_nal.update_layout(paper_bgcolor="#F8F9F9")

year_bar_plot_nal = []
for year in accidentes_por_year["Year"].unique():
    year_bar_plot_nal += [px.bar(accidentes_por_year[accidentes_por_year["Year"] == year], x="Departamento",
                                 y="AccidentesNormalizado", title="Accidentes año: "+str(year)+", \
                                (normalizado por millon de habitantes)")]


bar_plot_accidents = px.bar(accidentes_por_year, x="Year", y="AccidentesNormalizado",
                            title="Accidentes por año por millón de habitantes", color="Departamento", barmode='group')
bar_plot_accidents.update_layout(title="yearly accidents",
                                 paper_bgcolor="#F8F9F9")
bar_plot_accidents_w = px.bar(accidentes_por_dia_completo, x="DOW", y="AccidentesNormalizado",
                              title="Accidentes por dia de la semana (por Millón de habitantes)", color="Departamento", barmode='group')
bar_plot_accidents_w.update_layout(title="weekly accidents",
                                   paper_bgcolor="#F8F9F9")


year_accidets_day = []
for year in accidentes_por_dia["Year"].unique():
    year_accidets_day += [px.bar(accidentes_por_dia[accidentes_por_dia["Year"] == year], x="DOW", y="AccidentesNormalizado",
                                 title="Accidentes por dia de la semana (por Millón de habitantes) para el año "+str(year),
                                  color="Departamento", barmode='group')]


layout = html.Div([
    # html.H3('Page 1'),
    # html.P('here goes the national plots')
    html.Div(
        [
            # Place the main graph component here:
            dcc.Graph(figure=Map_Fig, id="US_map")
        ]),
    html.Div(
        [
            # Place the main graph component here:
            dcc.Graph(figure=Map_Fig_norm, id="US_map")
        ]),
    html.Div(
        [
            # Place the main graph component here:
            dcc.Graph(figure=bar_plot_nal, id="US_map")
        ]),
    html.Div(
        [
            dcc.Graph(figure=i, id="US_map") for i in year_bar_plot_nal
        ]),
    html.Div(
        [
            # Place the main graph component here:
            dcc.Graph(figure=bar_plot_accidents, id="US_map")
        ]),
    html.Div(
        [
            # Place the main graph component here:
            dcc.Graph(figure=bar_plot_accidents_w, id="US_map")
        ]),
    html.Div(
        [
            dcc.Graph(figure=i, id="US_map") for i in year_accidets_day
        ])
])


def page1_callbacks(app):
    pass
    # MAP date interaction
    # @app.callback(
    #     Output("US_map", "figure"),
    #     [Input("date_picker", "start_date"), Input("date_picker", "end_date")],
    # )
    # def update_map(start_date, end_date):
    #     dff = df[
    #         (df["Order Date"] >= start_date) & (df["Order Date"] < end_date)
    #     ]  # We filter our dataset for the daterange
    #     dff = dff.groupby("State_abbr").sum().reset_index()
    #     fig_map2 = px.choropleth_mapbox(
    #         dff,
    #         locations="State_abbr",
    #         color="Sales",
    #         geojson=geojson,
    #         zoom=3,
    #         mapbox_style="carto-positron",
    #         center={"lat": 37.0902, "lon": -95.7129},
    #         color_continuous_scale="Viridis",
    #         opacity=0.5,
    #         title="US Sales",
    #     )
    #     fig_map2.update_layout(
    #         title="US State Sales",
    #         margin={"r": 0, "t": 0, "l": 0, "b": 0},
    #         paper_bgcolor="#F8F9F9",
    #         plot_bgcolor="#F8F9F9",
    #     )
    #     return fig_map2

    # MAP click interaction

    # @app.callback(
    #     Output("state_dropdown", "value"),
    #     [Input("US_map", "clickData")],
    #     [State("state_dropdown", "value")],
    # )
    # def click_saver(clickData, state):
    #     if clickData is None:
    #         raise PreventUpdate

    #     # print(clickData)

    #     state.append(clickData["points"][0]["location"])

    #     return state
