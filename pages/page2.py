from dash import dcc, html, Input, Output, callback
import pandas as pd
import numpy as np
import plotly.express as px

from components.app import app




df_envigado = pd.read_csv("data/Envigado_final.csv", low_memory=False)
df_medellin = pd.read_csv("data/Medellin_final.csv", low_memory=False)


#Creamos LAT y LON con base a coordenadas
df_envigado["LAT"]=df_envigado["Coordenadas"].str.split(",").str[0].str[1:].str[:1]+"."+df_envigado["Coordenadas"].str.split(",").str[0].str[1:].str[1:-2]
df_envigado["LON"]=df_envigado["Coordenadas"].str.split(",").str[1].str[:-1].str[:4]+"."+df_envigado["Coordenadas"].str.split(",").str[1].str[:-3].str[4:]
df_envigado["LAT"]=df_envigado["LAT"].astype(float)
df_envigado["LON"]=df_envigado["LON"].astype(float)

#Eliminamos LAT y LON que no corresponden con la ciudad
df_envigado.loc[(df_envigado["LAT"]<6) | (df_envigado["LAT"]>6.2),"LAT"]=np.nan
df_envigado.loc[(df_envigado["LON"]<-77) | (df_envigado["LON"]>-75),"LON"]=np.nan

#Creamos LAT y LON con base a coordenadas
df_medellin["LON"]=df_medellin["Coordenadas"].str.split(",").str[0].str[1:]
df_medellin["LAT"]=df_medellin["Coordenadas"].str.split(",").str[1].str[:-1]
df_medellin["LAT"]=df_medellin["LAT"].astype(float)
df_medellin["LON"]=df_medellin["LON"].astype(float)


#Eliminamos LAT y LON que no corresponden con la ciudad
df_medellin.loc[(df_medellin["LAT"]<6) | (df_medellin["LAT"]>6.4),"LAT"]=np.nan
df_medellin.loc[(df_medellin["LON"]<-76) | (df_medellin["LON"]>-75),"LON"]=np.nan

df_heatmap_envigado = df_envigado.groupby(["LAT","LON"])["Fecha"].count().reset_index().rename(columns={"Fecha":"Cuenta"}).sort_values(["Cuenta"],ascending=False)
df_heatmap_medellin = df_medellin.groupby(["LAT","LON"])["Fecha"].count().reset_index().rename(columns={"Fecha":"Cuenta"}).sort_values(["Cuenta"],ascending=False)


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

