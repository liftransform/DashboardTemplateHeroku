from dash import html


def create_navbar(url = "/"):
    active = "bg-blue-100 text-gray-900"
    inactive = "hover:bg-gray-100 hover:text-gray-900"

    links = [
        {
            "name": "Home",
            "href": "/",
            "class": active if url == "/" else inactive,
        },
        {
            "name": "Page 2",
            "href": "/page-2",
            "class": active if url == "/page-2" else inactive,
        },
        {
            "name": "Page 3",
            "href": "/page-3",
            "class": active if url == "/page-3" else inactive,
        },
        {
            "name": "Page 4",
            "href": "/page-4",
            "class": active if url == "/page-4" else inactive,
        },
    ]

    children_links = []
    for link in links:
        children_links.append(
            html.A(
                link["name"],
                href=link["href"],
                className=link["class"] + " block px-4 py-2 text-sm text-gray-700",
            )
        )

    navbar = html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.H2(
                                "Dash Template",
                                className="text-xl font-bold text-gray-800",
                            ),
                        ]
                    )
                ],
                className="flex justify-between items-center",
            ),
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                children=children_links,
                                className="mt-2 space-y-2",
                            ),
                        ],
                        className="px-2 pt-2 pb-3 space-y-1",
                    ),
                ],
                className="flex flex-col w-100",
            ),
        ],
        className="flex flex-col h-screen bg-gray-100 w-[15%] py-5 px-3 shadow-sm",
    )

    return navbar
