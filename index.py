from dash import html, dcc
from dash.dependencies import Input, Output
from home import create_page_home
from page_2 import create_page_2
from page_3 import create_page_3
from page_4 import create_page_4
from app import app

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/page-2":
        return create_page_2(pathname)
    if pathname == "/page-3":
        return create_page_3(pathname)
    if pathname == "/page-4":
        return create_page_4(pathname)
    else:
        return create_page_home(pathname)


if __name__ == "__main__":
    app.run_server(
        debug=True
    )  # TODO: Change this to False when deploying to production
