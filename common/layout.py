from dash import html
from common.navbar import create_navbar


def create_layout(title="home page", url="/", children=[]):
    layout = html.Div(
        children=[
            create_navbar(url),
            html.Div(
                children=[
                    html.H3(f"Welcome to {title}!", className='text-2xl font-bold text-gray-800 capitalize'),
                    html.Div(children=children),
                ],
                className="flex flex-col gap-3 w-[90%] bg-gray-50 border-r border-green-200 py-5 px-5 overflow-y-auto",
            ),
        ],
        className="w-100 h-screen flex overflow-hidden",
    )
    return layout
