from dash import html, dcc
from common.layout import create_layout
from common.grid import create_grid, create_grid_item
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
                    create_grid_item(dcc.Graph("k1", figure=fig),2),
                    create_grid_item(dcc.Graph("k2", figure=fig)),
                    create_grid_item(dcc.Graph("k3", figure=fig)),
                    create_grid_item(dcc.Graph("k4", figure=fig),2),
                ],
            )
        ],
    )
    return layout
