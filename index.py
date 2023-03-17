from dash import html, dcc
from dash.dependencies import Input, Output
from pages import pages, create_page
from app import app

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    for page in pages:
        if pathname == page["pathname"]:
            return create_page([page["page"](pathname)])


if __name__ == "__main__":
    # set debug=True to enable hot reloading
    app.run_server()
