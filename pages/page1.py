from datetime import date
from sqlite3 import Row

from numpy import NAN
from components.constants import LOGO

from components.styles import *
from dash.exceptions import PreventUpdate
from dash import dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
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
departments = ['San Andres y Providencia', 'Valle del Cauca', 'Cundinamarca', 'Casanare', 'Magdalena', 'Cesar', 'Meta', 'Boyacá', 'Nariño', 'Norte de Santander', 'Quindío', 'Risaralda',
               'Huila', 'Antioquia', 'Caldas', 'Caquetá', 'Santander', 'Tolima', NAN, 'Cauca', 'Guajira', 'Putumayo', 'Bolívar', 'Chocó', 'Sucre', 'Ocaña', 'Atlántico', 'Córdoba', 'Planta Central']

map_df = geopandas.read_file('data/nacional/accidentes.geojson')
accidentes_por_year = pd.read_csv("data/nacional/accidentes_por_year.csv")
accidentes_total = pd.read_csv("data/nacional/accidentes_total.csv")
accidentes_por_dia = pd.read_csv("data/nacional/accidentes_por_dia.csv")
accidentes_por_dia_completo = pd.read_csv(
    "data/nacional/accidentes_por_dia_completo.csv")

df_Nacional = pd.read_csv('data/nacional/Nacional_final.csv')
df_Nacional = df_Nacional.rename(columns={
                                 "Cuenta Heridos": "Cuenta heridos", "Cuenta Muertos": "Cuenta muertos", "Ciudad": "Departamento"})
df_Poblacion = pd.read_csv('data/poblacion_departamentos.csv', sep=';')

# variable para filtrar por departamento  ['San Andres y Providencia', 'Valle del Cauca', 'Cundinamarca', 'Casanare', 'Magdalena', 'Cesar', 'Meta', 'Boyacá', 'Nariño', 'Norte de Santander', 'Quindío', 'Risaralda', 'Huila', 'Antioquia', 'Caldas', 'Caquetá', 'Santander', 'Tolima', nan, 'Cauca', 'Guajira', 'Putumayo', 'Bolívar', 'Chocó', 'Sucre', 'Ocaña', 'Atlántico', 'Córdoba', 'Planta Central']
departamento = "Antioquia"
parametro = "Muertos"  # variable para filtar por Heridos o Muertos
# variable para seleccionar intervalo de tiempo a graficar: ["Year","Month","DOW"]
elemento_fecha = "Month"
elemento_x = 'Clima'  # ['Clase accidente','Clima']
# con esto se puede escoger entre porcentaje y nominal el valor que se muestra en el eje y. ['Porcentaje','Accidentes']
valor = "Porcentaje"
elemento_y = "Cuenta muertos"


Map_Fig_norm = px.choropleth(map_df, geojson=map_df.geometry,
                             locations=map_df.index, color="AccidentesNormalizado")
Map_Fig_norm.update_geos(fitbounds="locations", visible=True)
Map_Fig_norm.update_layout(title="Normalized National highway's accidents")


# Procesamiento de datos:

base = df_Nacional.loc[df_Nacional["Departamento"] == departamento]
if elemento_fecha == "Year":
    base = base.groupby([pd.to_datetime(base["Fecha"]).dt.year, parametro])["Unnamed: 0"].count(
    ).reset_index().rename(columns={"Fecha": "Year", "Unnamed: 0": "Accidentes"})
elif elemento_fecha == "Month":
    base = base.groupby([pd.to_datetime(base["Fecha"]).dt.month, parametro])["Unnamed: 0"].count(
    ).reset_index().rename(columns={"Fecha": "Month", "Unnamed: 0": "Accidentes"})
elif elemento_fecha == "DOW":
    base = base.groupby(["DOW", parametro])["Unnamed: 0"].count().reset_index(
    ).rename(columns={"Fecha": "Year", "Unnamed: 0": "Accidentes"})


base[parametro] = base[parametro].astype("str")

# Grafico:

graph_date_nal = px.bar(base,
                    x=elemento_fecha,
                    y="Accidentes",
                    color=parametro,
                    barmode="group",
                    text="Accidentes",
                    title="Diagrama de barras para accidentes con \n" + parametro + " en "+departamento+" por "+elemento_fecha)
graph_date_nal.update_xaxes(dtick=1)


base2 = df_Nacional.loc[df_Nacional["Departamento"] == departamento]
base2 = base2.groupby([elemento_x, parametro])["Unnamed: 0"].count(
).reset_index().rename(columns={"Fecha": "Year", "Unnamed: 0": "Accidentes"})
base2[parametro] = base2[parametro].astype("str")
base2["Porcentaje"] = base2.groupby(elemento_x)["Accidentes"].apply(
    lambda x: round(x/x.sum()*100, 2))

graph_cat = px.bar(base2,
                   x=elemento_x,
                   y=valor,
                   color=parametro,
                   barmode="group",
                   title="Diagrama de barras para accidentes con \n" +
                   parametro + " en "+departamento + " según " + elemento_x
                   )


base3 = df_Nacional.copy(deep=True)
base3 = base3.loc[base3["Fecha"].notnull(), ]



base3["Year"] = pd.to_datetime(
    base3["Fecha"]).dt.year.astype("int").astype("str")
base3["Month"] = pd.to_datetime(
    base3["Fecha"]).dt.month.astype("int").astype("str")
base3.groupby(["Month", "Departamento"])["Cuenta heridos"].sum().reset_index()

graph_3 = px.box(base3, y=elemento_y, x='Departamento',
                 color="Month", points='all')
# fig = px.box(base, y=elemento_y, x='Departamento',color = elemento_fecha,points='all')
graph_3.update_xaxes(dtick=1)


layout = dbc.Container([
    dbc.Row([
        dbc.Col([

            dcc.Graph(figure=Map_Fig_norm, id="heat_map")


        ], width={'size': 7, 'offset': 0}),

        dbc.Col([
            dbc.Row([
                dcc.Graph(figure=graph_date_nal, id="graph_date_nal")
            ])
        ], width={'size': 5, 'offset': 0}),
    ]),
    html.H5(""),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=graph_cat, id="graph_cat")
        ], width={'size': 12, 'offset': 0})

    ]),
    html.H5(""),
    dbc.Row([
        dbc.Col([
            dcc.Graph(figure=graph_3, id="graph_3")


        ], width={'size': 12, 'offset': 0})

    ])


], fluid=True)



depart = dcc.Dropdown(
    options=departments,
    value=[],
    id='departamento_dropdown',
    multi=False,
    style={'color': 'black'})

interval = dcc.Dropdown(
    options=['Year', "Month", "DOW"],
    value=['Year'],
    id='interval_dropdown',
    multi=False,
    style={'color': 'black'})


param = dcc.Dropdown(
    options=['Heridos', 'Muertos'],
    value=['Heridos'],
    id='param_dropdown',
    multi=False,
    style={'color': 'black'})

param2 = dcc.Dropdown(
    options=['Clase accidente', 'Clima'],
    value=['Clima'],
    id='param2_dropdown',
    multi=False,
    style={'color': 'black'})


sidebar = html.Div(
    [
        html.Img(src=LOGO, width="150px",
                 style={'textAlign': 'center'}),
        html.Hr(),
        html.H5("Departments"),
        depart,
        html.H5("Graph the interval"),
        interval,
        html.H5("Type of victim"),
        param,
        html.H5("2nd Row graph"),
        param2,


    ],
    id="sidebar",
    style=SIDEBAR_HIDEN,
)





def page1_callbacks(app):
    @app.callback(
        Output("graph_date_nal", "figure"),
        Input("departamento_dropdown", "value"),
        Input("interval_dropdown", "value"),
        Input("param_dropdown", "value"),

    )
    def filter_departments(departamento_dropdown, interval_dropdown, param_dropdown):
        if not departamento_dropdown or not interval_dropdown or not param_dropdown:
            raise PreventUpdate
        else:
            departamento = departamento_dropdown
            elemento_fecha = interval_dropdown
            parametro = param_dropdown

        base = df_Nacional.query("Departamento in @departamento")
        #loc[df_Nacional["Departamento"] == departamento]
        if elemento_fecha == "Year":
            base = base.groupby([pd.to_datetime(base["Fecha"]).dt.year, parametro])["Unnamed: 0"].count(
            ).reset_index().rename(columns={"Fecha": "Year", "Unnamed: 0": "Accidentes"})
        elif elemento_fecha == "Month":
            base = base.groupby([pd.to_datetime(base["Fecha"]).dt.month, parametro])["Unnamed: 0"].count(
            ).reset_index().rename(columns={"Fecha": "Month", "Unnamed: 0": "Accidentes"})
        elif elemento_fecha == "DOW":
            base = base.groupby(["DOW", parametro])["Unnamed: 0"].count().reset_index(
            ).rename(columns={"Fecha": "Year", "Unnamed: 0": "Accidentes"})

        base[parametro] = base[parametro].astype("str")

        # Grafico:

        graph_date = px.bar(base,
                            x=elemento_fecha,
                            y="Accidentes",
                            color=parametro,
                            barmode="group",
                            text="Accidentes",
                            title="Diagrama de barras para accidentes con \n" + str(parametro) + " en "+str(departamento)+" por "+str(elemento_fecha))
        graph_date.update_xaxes(dtick=1)
        return graph_date
    @app.callback(
        Output('graph_cat','figure'),
        Input('departamento_dropdown','value'),
        Input('param2_dropdown','value'),
        Input('param_dropdown','value'),
    )
    def filter_categories(departamento_dropdown,param2_dropdown,param_dropdown):

        if not departamento_dropdown or not param2_dropdown  or not param_dropdown:
            raise PreventUpdate
        else:
            departamento = departamento_dropdown
            elemento_x = param2_dropdown
            parametro = param_dropdown

        base2 = df_Nacional.loc[df_Nacional["Departamento"] == departamento]
        base2 = base2.groupby([elemento_x, parametro])["Unnamed: 0"].count(
        ).reset_index().rename(columns={"Fecha": "Year", "Unnamed: 0": "Accidentes"})
        base2[parametro] = base2[parametro].astype("str")
        base2["Porcentaje"] = base2.groupby(elemento_x)["Accidentes"].apply(
            lambda x: round(x/x.sum()*100, 2))

        graph_cat = px.bar(base2,
                        x=elemento_x,
                        y=valor,
                        color=parametro,
                        barmode="group",
                        title="Diagrama de barras para accidentes con \n" +
                        parametro + " en "+str(departamento) + " según " + str(elemento_x)
                        )
        return graph_cat
