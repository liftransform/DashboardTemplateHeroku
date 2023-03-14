from dash import html,dcc
from navbar import create_navbar

nav = create_navbar()
header = html.H3('Welcome to page 2 jkk!')
import pandas as pd
import plotly_express as px
nav = create_navbar()

data = pd.DataFrame({
    "names":['john','nobert','alex'],
    "age":[23,45,10]
})
fig = px.bar(data,x = "names",y = "age",color = "names")

def create_page_2():
    layout = html.Div([
        nav,
        header,
    dcc.Graph("k1",figure = fig),
    dcc.Graph("k2",figure = fig),
    dcc.Graph("k3",figure = fig),
    ])
    return layout