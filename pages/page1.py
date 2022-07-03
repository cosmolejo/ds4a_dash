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


df_Nacional = pd.read_csv('data/Nacional_final.csv')
df_Nacional = df_Nacional.rename(columns={"Cuenta Heridos":"Cuenta heridos","Cuenta Muertos":"Cuenta muertos","Ciudad":"Departamento"})
df_Poblacion = pd.read_csv('data/poblacion_departamentos.csv',sep=';')

base = df_Nacional.groupby(["Fecha","Departamento"])["Heridos"].count().reset_index().rename(columns={"Heridos":"Accidentes"})
base["Fecha"]=pd.to_datetime(base['Fecha'])
base["Year"]=base["Fecha"].dt.year
base["Month"]=base["Fecha"].dt.month
base["DOW"]=base["Fecha"].dt.dayofweek+1

accidentes_por_year = base.groupby(["Departamento","Year"]).sum().drop(columns=["Month","DOW"]).reset_index()
accidentes_por_year = accidentes_por_year.merge(df_Poblacion[["Departamento","Habitantes"]],how='left',on="Departamento")
accidentes_por_year["AccidentesNormalizado"]=accidentes_por_year["Accidentes"]/accidentes_por_year["Habitantes"]*1e6

accidentes_total = accidentes_por_year.groupby(["Departamento","Habitantes"]).sum().drop(columns=["Year"]).reset_index()


accidentes_por_dia = base.groupby(["Departamento","Year","DOW"])["Accidentes"].sum().reset_index()
accidentes_por_dia = accidentes_por_dia.merge(df_Poblacion[["Departamento","Habitantes"]],how='left',on="Departamento")
accidentes_por_dia["AccidentesNormalizado"]=accidentes_por_dia["Accidentes"]/accidentes_por_dia["Habitantes"]*1e6
accidentes_por_dia = accidentes_por_dia.sort_values(["Year","Departamento"])

myshpfile = geopandas.read_file('data/depto.shp')
myshpfile.set_index('DPTO', drop=True, inplace=True)
myshpfile = myshpfile.rename(columns={"NOMBRE_DPT":"Departamento"})
dict = {"ANTIOQUIA": "Antioquia", 
        "ATLANTICO": "Atlántico",
        "SANTAFE DE BOGOTA D.C":"Bogotá, D.C.",
        "BOLIVAR":"Bolívar",
        "BOYACA":"Boyacá",
        "CALDAS":"Caldas",
        "CAQUETA":"Caquetá",
        "CAUCA":"Cauca",
        "CESAR":"Cesar",
        "CORDOBA":"Córdoba",
        "CUNDINAMARCA":"Cundinamarca",
        "CHOCO":"Chocó",
        "HUILA":"Huila",
        "LA GUAJIRA":"Guajira",
        "MAGDALENA":"Magdalena",
        "META":"Meta",
        "NARIÑO":"Nariño",
        "NORTE DE SANTANDER":"Norte de Santander",
        "QUINDIO":"Quindío",
        "RISARALDA":"Risaralda",
        "SANTANDER":"Santander",
        "SUCRE":"Sucre",
        "TOLIMA":"Tolima",
        "VALLE DEL CAUCA":"Valle del Cauca",
        "ARAUCA":"Arauca",
        "CASANARE":"Casanare",
        "PUTUMAYO":"Putumayo",
        "AMAZONAS":"Amazonas",
        "GUAINIA":"Guainia",
        "GUAVIARE":"Guaviare",
        "VAUPES":"Vaupes",
        "VICHADA":"Vichada",
        "ARCHIPIELAGO DE SAN ANDRES PROVIDENCIA Y SANTA CATALINA":"San Andres y Providencia",
    }

myshpfile = myshpfile.replace({"Departamento": dict})
myshpfile = myshpfile.merge(accidentes_total[["Departamento","Accidentes","AccidentesNormalizado"]],how='left',on="Departamento")
myshpfile['Accidentes'] = myshpfile['Accidentes'].fillna(0)
myshpfile['AccidentesNormalizado'] = myshpfile['AccidentesNormalizado'].fillna(0)
myshpfile.set_index('Departamento', inplace=True)

map_df = myshpfile
map_df.to_crs(pyproj.CRS.from_epsg(4326), inplace=True)




Map_Fig =  px.choropleth(map_df, geojson=map_df.geometry,locations=map_df.index, color="Accidentes")
Map_Fig.update_geos(fitbounds="locations", visible=True)
Map_Fig.update_layout(title="National highway's accidents", paper_bgcolor="#F8F9F9")


layout = html.Div([
    #html.H3('Page 1'),
    #html.P('here goes the national plots')
    html.Div(
    [
        # Place the main graph component here:
        dcc.Graph(figure=Map_Fig, id="US_map")
    ]
)
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