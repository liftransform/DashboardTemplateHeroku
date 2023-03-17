"""_summary_line
    All the pages will be added to this folder.
"""
from dash import html, dcc
from .home import create_home
from .page_2 import create_page_2
from .page_3 import create_page_3
from .page_4 import create_page_4

# pages
pages = [
    {"name": "Home", "pathname": "/", "page": create_home},
    {"name": "Page 2", "pathname": "/page-2", "page": create_page_2},
    {"name": "Page 3", "pathname": "/page-3", "page": create_page_3},
    {"name": "Page 4", "pathname": "/page-4", "page": create_page_4},
]


def create_page(children=[]):
    return html.Main(children=children, className="w-full h-full")
