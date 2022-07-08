from datetime import date
from html.entities import html5
from dash import dcc, html, Input, Output, callback
import pandas as pd
import numpy as np
import plotly.express as px
from dash.exceptions import PreventUpdate

from components.app import app
from components.constants import LOGO
from components.styles import *

heat_list = ['barranquilla','envigado','palmira','medellin']

df_heatmap_barranquilla = pd.read_csv("data/local/df_heatmap_barranquilla.csv", low_memory=False)
df_heatmap_envigado = pd.read_csv("data/local/df_heatmap_envigado.csv", low_memory=False)
df_heatmap_palmira = pd.read_csv("data/local/df_heatmap_palmira.csv", low_memory=False)
df_heatmap_medellin = pd.read_csv("data/local/df_heatmap_medellin.csv", low_memory=False)



df_Barranquilla = pd.read_csv('data/local/Barranquilla_final.csv', low_memory=False)
df_Bucaramanga = pd.read_csv('data/local/Bucaramanga_final.csv', low_memory=False)
df_Envigado = pd.read_csv('data/local/Envigado_final.csv', low_memory=False)
df_Palmira = pd.read_csv('data/local/Palmira_final.csv', low_memory=False)
df_Medellin = pd.read_csv('data/local/Medellin_final.csv', low_memory=False)

df_Bucaramanga=df_Bucaramanga.rename(columns={"Cuenta Heridos":"Cuenta heridos","Cuenta Muertos":"Cuenta muertos"})
df_Envigado=df_Envigado.rename(columns={"Cuenta Heridos":"Cuenta heridos","Cuenta Muertos":"Cuenta muertos"})
df_Medellin=df_Medellin.rename(columns={"Cuenta Heridos":"Cuenta heridos","Cuenta Muertos":"Cuenta muertos"})

df_ciudades = pd.concat([df_Barranquilla,df_Bucaramanga,df_Envigado,df_Palmira,df_Medellin])




ciudad = "Barranquilla" ##variable para filtrar por departamento ['Barranquilla', 'Bucaramanga', 'Envigado', 'Palmira', 'Medellin']
parametro = "Muertos" ##variable para filtar por Heridos o Muertos ['Muertos', 'Heridos']
elemento_fecha = "Month" ##variable para modificar el gráfico en año, mes o DOW (dia de la semana) ["Year","Month","DOW"]



envigado_heat = px.density_mapbox(df_heatmap_envigado, lat='LAT', lon='LON', z='Cuenta', radius=10,
                        center=dict(lat=6.17, lon=-75.58), zoom=13,
                        mapbox_style="stamen-terrain")

envigado_heat.update_layout(title=f"{ciudad} accident heatmap", paper_bgcolor="#F8F9F9")

medellin_heat = px.density_mapbox(df_heatmap_medellin, lat='LAT', lon='LON', z='Cuenta', radius=10,
                        center=dict(lat=6.25, lon=-75.60), zoom=11,
                        mapbox_style="stamen-terrain")
medellin_heat.update_layout(title=f"{ciudad} accident heatmap", paper_bgcolor="#F8F9F9")

barranquilla_heat = px.density_mapbox(df_heatmap_barranquilla, lat='LAT', lon='LON', z='Cuenta', radius=10,
                        center=dict(lat=11, lon=-74.80), zoom=10,
                        mapbox_style="stamen-terrain")
barranquilla_heat.update_layout(title=f"{ciudad} accident heatmap", paper_bgcolor="#F8F9F9")

palmira_heat = px.density_mapbox(df_heatmap_palmira, lat='LAT', lon='LON', z='Cuenta', radius=10,
                         center=dict(lat=3.53, lon=-76.30), zoom=12,
                        mapbox_style="stamen-terrain")
palmira_heat.update_layout(title=f"{ciudad} accident heatmap", paper_bgcolor="#F8F9F9")

#['barranquilla','envigado','palmira','medellin']
heats = {
    'barranquilla' : barranquilla_heat,
    'envigado' : envigado_heat,
    'palmira' : palmira_heat,
    'medellin' : medellin_heat
}


base = df_ciudades.loc[df_ciudades["Ciudad"]==ciudad]

if elemento_fecha == "Year":
    base = base.groupby([pd.to_datetime(base["Fecha"]).dt.year,parametro])["Unnamed: 0"].count().reset_index().rename(columns={"Fecha":"Year","Unnamed: 0":"Accidentes"})
elif elemento_fecha == "Month":
    base = base.groupby([pd.to_datetime(base["Fecha"]).dt.month,parametro])["Unnamed: 0"].count().reset_index().rename(columns={"Fecha":"Month","Unnamed: 0":"Accidentes"})
elif elemento_fecha == "DOW":
    base = base.groupby(["DOW",parametro])["Unnamed: 0"].count().reset_index().rename(columns={"Fecha":"Year","Unnamed: 0":"Accidentes"})
    
    
base[parametro]=base[parametro].astype("str")

graph_date = px.bar(base,
             x=elemento_fecha,
             y="Accidentes",
             color=parametro,
             barmode="group",
             text = "Accidentes",
            title = "Diagrama de barras para accidentes con "+ parametro + " en "+ciudad+" por "+elemento_fecha)
graph_date.update_xaxes(dtick = 1)



layout = html.Div([
#     html.H3('Page 2'),
#    html.P('here goes the local plots')
html.Div(
    [
        # Place the main graph component here:
        dcc.Graph(figure=barranquilla_heat, id="graph_heat")
    ]),
    html.Div(
    [
        # Place the main graph component here:
        dcc.Graph(figure=graph_date, id="graph_date")
    ])
])




date_picker = dcc.DatePickerRange(
            id="my-date-picker-range",
            min_date_allowed=date(1995, 8, 5),
            max_date_allowed=date(2017, 9, 19),
            initial_visible_month=date(2017, 8, 5),
            end_date=date(2017, 8, 25),
            style=DATE_PICKER_STYLE,
        )

heat_cities = dcc.Dropdown(
    options= heat_list,
    value=['barranquilla'],
    id='heat_cities',
    multi=False,
    style = {'color':'black'})

bar_cities = dcc.Dropdown(
    options=['Barranquilla', 'Bucaramanga', 'Envigado', 'Palmira', 'Medellin'],
    value=['Barranquilla'],
    id='bar_cities',
    multi=False,
    style = {'color':'black'})


interval = dcc.Dropdown(
    options=['Year', "Month", "DOW"],
    value=['Year'],
    id='interval',
    multi=False,
    style = {'color':'black'})

param = dcc.Dropdown(
    options=['Heridos', 'Muertos'],
    value=['Heridos'],
    id='param',
    multi=False,
    style = {'color':'black'})

sidebar = html.Div(
    [
        html.Img(src=LOGO, width="200px", style={'textAlign':'center'}),
        html.Hr(),
        html.H5("Heatmap city"),
        heat_cities,
        html.H5('Barplot city'),
        bar_cities,
         html.H5("Graph the interval"),
        interval,
        html.H5("Type of victim"),
        param,

        
    ],
    id="sidebar",
    style=SIDEBAR_STYLE,
)


def page2_callbacks(app):
    @app.callback(
        Output('graph_heat','figure'),
        Input('heat_cities','value'),
      
    )
    def filter_heat(heat_cities):
        if not heat_cities:
            raise PreventUpdate
        else:
            graph_heat = heats[heat_cities]
            return graph_heat
    @app.callback(
        Output('graph_date','figure'),
         Input('bar_cities','value'),
        Input('interval','value'),
        Input('param','value')
    )
    def filter_bar(bar_cities,interval,param):
        if not bar_cities:
           raise PreventUpdate
        else:
            ciudad = bar_cities
        if not interval:
            raise PreventUpdate
        else:
            elemento_fecha = interval
        if not param:
            raise PreventUpdate
        else:
            parametro = param

        base = df_ciudades.query('Ciudad in @ciudad')
        #loc[df_ciudades["Ciudad"]==ciudad]

        if elemento_fecha == "Year":
            base = base.groupby([pd.to_datetime(base["Fecha"]).dt.year,parametro])["Unnamed: 0"].count().reset_index().rename(columns={"Fecha":"Year","Unnamed: 0":"Accidentes"})
        elif elemento_fecha == "Month":
            base = base.groupby([pd.to_datetime(base["Fecha"]).dt.month,parametro])["Unnamed: 0"].count().reset_index().rename(columns={"Fecha":"Month","Unnamed: 0":"Accidentes"})
        elif elemento_fecha == "DOW":
            base = base.groupby(["DOW",parametro])["Unnamed: 0"].count().reset_index().rename(columns={"Fecha":"Year","Unnamed: 0":"Accidentes"})
            
            
        base[parametro]=base[parametro].astype("str")

        graph_date = px.bar(base,
                    x=elemento_fecha,
                    y="Accidentes",
                    color=parametro,
                    barmode="group",
                    text = "Accidentes",
                    title = "Diagrama de barras para accidentes con "+ parametro + " en "+ciudad+" por "+elemento_fecha)
        graph_date.update_xaxes(dtick = 1)

        return graph_date