from dash import dcc, html, Input, Output, callback
from components.constants import *
from components.navbar import *
from components.app import app
import dash_bootstrap_components as dbc


navbar_callbacks(app)
layout = html.Div([
    dbc.Row([
        dbc.Col([
            html.H1('Crash Analytics',
                    className="text-center font-weight-bold text-danger"
                    )
        ],
            width=12

        )

    ]),
    dbc.Row([
        dbc.Col([
            html.Img(src=LOGO,
                     width="300px",
                     className="text-center"
                     )
        ],
            width=12,
            style={'textAlign': 'center'}

        )

    ]),
    dbc.Row([
        dbc.Col([
            html.H3(
                'A car accident analysis made with open data from the Colombian government')
        ],
            width=12,
            style={'textAlign': 'center'}

        )

    ]),   dbc.Row([
        dbc.Col([
            html.H3(
                '')
        ],
            width=12,
            style={'textAlign': 'center'}

        )

    ]),dbc.Row([
        dbc.Col([
            html.H3(
                '')
        ],
            width=12,
            style={'textAlign': 'center'}

        )

    ]),dbc.Row([
        dbc.Col([
            html.H3(
                '')
        ],
            width=12,
            style={'textAlign': 'center'}

        )

    ]),
    dbc.Row([
        dbc.Col([
            html.Img(src=DS4A,
                     width="300px",
                     className="text-center"
                     )
        ],
            width=12,
            style={'textAlign': 'center',
                   }

        )
    ])

])
