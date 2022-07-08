from dash import dcc, html, Input, Output, callback
from components.constants import *
import dash_bootstrap_components as dbc

from components.styles import *

layout = dbc.Container([
    dbc.Row([
        dbc.Col(

            dbc.Card([
                html.Img(src=ALEJANDRO,
                         className='card-img-top',
                         style=CARD_IMG_STYLE),
                dbc.CardBody([
                    html.H5(
                        'Alejandro Mesa',
                        className="card-title",
                        style=CARD_TITLE
                    ),
                    html.P(
                        'Data science and engineering M.Sc. Student @Politecnico di Torino',
                        className="card-text"
                    ),
                    html.A(html.Span([
                        "LinkedIn",
                        html.I(className="fab fa-linkedin")
                    ]),
                        href="https://www.linkedin.com/in/alejandro-mesa95/",
                        className="btn bi bi-linkedin",
                        target="_blank",
                        style=CARD_BUTTON)
                ])
            ], style=CARD_STYLE)
        ),
        dbc.Col(

            dbc.Card([
                html.Img(src=DANIEL,
                         className='card-img-top',
                         style=CARD_IMG_STYLE),
                dbc.CardBody([
                    html.H5(
                        'Daniel Acosta',
                        className="card-title",
                        style=CARD_TITLE
                    ),
                    html.P(
                        ' Industrial engineer, data analyst. ',
                        className="card-text"
                    ),
                    html.A(
                        html.Span([
                            "LinkedIn",
                            html.I(className="fab fa-linkedin")
                        ]),
                        href="https://www.linkedin.com/in/daniel-acosta-industrial",
                        className="btn",
                        target="_blank",
                        style=CARD_BUTTON)
                ])
            ], style=CARD_STYLE)
        ),
        dbc.Col(

            dbc.Card([
                html.Img(src=JOSE,
                         className='card-img-top',
                         style=CARD_IMG_STYLE),
                dbc.CardBody([
                    html.H5(
                        'José Moreno',
                        className="card-title",
                        style=CARD_TITLE
                    ),
                    html.P(
                        'Electronic engineer',
                        className="card-text"
                    ),
                    html.A(
                        html.Span([
                            "LinkedIn",
                            html.I(className="fab fa-linkedin")
                        ]),
                        href="https://www.linkedin.com/in/jose-a-moreno-c/",
                        className="btn",
                        target="_blank",
                        style=CARD_BUTTON)
                ])
            ], style=CARD_STYLE)
        ),
        dbc.Col(

            dbc.Card([
                html.Img(src=CARLOS,
                         className='card-img-top',
                         style=CARD_IMG_STYLE),
                dbc.CardBody([
                    html.H5(
                        'Carlos Gabriel Salas',
                        className="card-title",
                        style=CARD_TITLE
                    ),
                    html.P(
                        'Physicist interested in condensed matter and data analysis.',
                        className="card-text"
                    ),
                    html.A(
                        html.Span([
                            "LinkedIn",
                            html.I(className="fab fa-linkedin")
                        ]),
                        href="https://www.linkedin.com/in/carlos-gabriel-salas-murillo",
                        className="btn",
                        target="_blank",
                        style=CARD_BUTTON)
                ])
            ], style=CARD_STYLE)
        ),



    ]),

    dbc.Row([
        dbc.Col(

            dbc.Card([
                html.Img(src=AUGUSTO,
                         className='card-img-top',
                         style=CARD_IMG_STYLE),
                dbc.CardBody([
                    html.H5(
                        'Augusto Uribe',
                        className="card-title",
                        style=CARD_TITLE
                    ),
                    html.P(
                        'Electronic engineer interested in telecommunications and data science',
                        className="card-text"
                    ),
                    html.A(html.Span([
                        "LinkedIn",
                        html.I(className="fab fa-linkedin")
                    ]),
                        href="https://www.linkedin.com/in/james-augusto-uribe-naranjo-13273610b",
                        className="btn bi bi-linkedin",
                        target="_blank",
                        style=CARD_BUTTON)
                ])
            ], style=CARD_STYLE)
        ),
        dbc.Col(

            dbc.Card([
                html.Img(src=ALEJANDRA,
                         className='card-img-top',
                         style=CARD_IMG_STYLE),
                dbc.CardBody([
                    html.H5(
                        'Alejandra Cano',
                        className="card-title",
                        style=CARD_TITLE
                    ),
                    html.P(
                        'Pharmacist. Msc Pharmaceutical and Alimentary Sciences.',
                        className="card-text"
                    ),
                    html.A(
                        html.Span([
                            "LinkedIn",
                            html.I(className="fab fa-linkedin")
                        ]),
                        href=" https://www.linkedin.com/in/alejandra-cano-26b1b31b1/",
                        className="btn",
                        target="_blank",
                        style=CARD_BUTTON)
                ])
            ], style=CARD_STYLE)
        ),
        dbc.Col(

            dbc.Card([
                html.Img(src=MARIA,
                         className='card-img-top',
                         style=CARD_IMG_STYLE),
                dbc.CardBody([
                    html.H5(
                        'Maria Isabel Rosales',
                        className="card-title",
                        style=CARD_TITLE
                    ),
                    html.P(
                        'System and Computer Engineer',
                        className="card-text"
                    ),
                    html.A(
                        html.Span([
                            "LinkedIn",
                            html.I(className="fab fa-linkedin")
                        ]),
                        href="https://www.linkedin.com/in/maria-isabel-rosales-silva-a189741aa/?locale=en_US",
                        className="btn",
                        target="_blank",
                        style=CARD_BUTTON)
                ])
            ], style=CARD_STYLE)
        )
    ])




])
