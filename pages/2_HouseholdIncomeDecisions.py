import dash
from dash import html,dcc
import plotly_express as px
import pandas as pd
import warnings


warnings.filterwarnings("ignore")
from oauth2client.service_account import ServiceAccountCredentials
external_scripts=["https://cdn.tailwindcss.com"]
dash.register_page(__name__,external_scripts="external_scripts")

data = pd.DataFrame({
    "names":['john','nobert','alex'],
    "age":[23,45,10]
})
fig = px.bar(data,x = "names",y = "age")

layout = html.Div(className = "w-full p-2  flex items-center justify-between gap-4 mt-12",
    children=[html.Div(
                    children=[html.Div(dcc.Graph(id="1",figure=fig)),
                              html.Div(dcc.Graph(id="2",figure=fig)),
                              html.Div(dcc.Graph(id="3",figure=fig))])])

