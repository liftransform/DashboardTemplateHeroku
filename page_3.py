from dash import html, dcc
from layout import create_layout
from grid import create_grid
import pandas as pd
import plotly_express as px


data = pd.DataFrame({"names": ["john", "nobert", "alex"], "age": [23, 45, 10]})
fig = px.bar(data, x="names", y="age", color="names")


def create_page_3(pathname):
    layout = create_layout(
        "page 3! jkk",
        pathname,
        [
            create_grid(
                3,
                [
                    dcc.Graph("k1", figure=fig),
                    dcc.Graph("k2", figure=fig),
                    dcc.Graph("k3", figure=fig),
                    dcc.Graph("k4", figure=fig),
                ],
            )
        ],
    )
    return layout
