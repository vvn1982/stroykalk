import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import numpy as np, pandas as pd
from assets import layout_parts

# set app variable with dash, set external style to bootstrap theme
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SOLAR],
    meta_tags=[{"name": "viewport",
                "content": "width=device-width, initial-scale=1, maximum-scale=1.2, minimum-scale=0.9"
                }],
)
app.title = "Калькулятор смет для стройки и ремонта"
# set app server to variable for deployment
srv = app.server

# set app callback exceptions to true
app.config.suppress_callback_exceptions = True



app.layout =  dbc.Container(
    [
        # navbar(),
        html.H1("Смета ремонта"),
        html.Hr(),
        # Выбор видов работ для сметы
        layout_parts.layout_work_type_groups_tabs(),
        # Ввод пользователем размеров комнаты


        #
        dbc.Row(
            [
                "VVN1982@mail.ru"
            ],
            align="center",
        ),
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)
