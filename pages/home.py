from dash import html, dcc
from common.layout import create_layout


def create_home(pathname):
    layout = html.Div(
        [
            create_layout(
                "home page",
                pathname,
                [
                    html.Div(
                        children=[
                            html.Div(
                                [
                                    html.P(
                                        "This is a template for Dash apps using Dash Bootstrap Components and Tailwind CSS."
                                    ),
                                    html.P("The navbar is created using Tailwind CSS."),
                                    html.P(
                                        "The layout is created using Dash Bootstrap Components."
                                    ),
                                    html.P(
                                        "The content is created using Dash HTML Components."
                                    ),
                                ]
                            ),
                        ],
                        className="flex flex-col w-full mt-2",
                    ),
                ],
            )
        ]
    )
    return layout
