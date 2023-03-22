from dash import html, dcc
from common.layout import create_layout
from common.grid import create_grid, create_grid_item
from common.card_detail import create_card


def create_home(pathname):
    layout = html.Div(
        [
            create_layout(
                "",
                pathname,
                [
                    html.Div(
                        children=[
                            create_grid(
                                3,
                                children=[
                                    create_grid_item(
                                        children=[
                                            html.Div(
                                                className="min-h-[50vh] flex justify-center items-center px-16 gap-4 relative",
                                                children=[
                                                    html.Div(
                                                        className="absolute h-72 w-72 bg-[#EBCABA] opacity-60 rounded-lg z-0",
                                                    ),
                                                    html.Div(
                                                        className="w-1/2 z-10",
                                                        children=[
                                                            html.H1(
                                                                "Look beyond the Limits.",
                                                                className="text-8xl font-black text-gray-800",
                                                            ),
                                                            html.P(
                                                                className="text-gray-600 mt-2 text-2xl",
                                                                children=[
                                                                    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptate."
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                    html.Div(
                                                        className="w-1/2 z-10 relative overflow-hidden",
                                                        children=[
                                                            html.Div(
                                                                className="absolute h-full w-full bg-gray-900 opacity-30 rounded-lg z-0",
                                                            ),
                                                            html.Img(
                                                                src="/assets/images/hero.jpg",
                                                                alt="hero",
                                                                className="w-full h-full object-cover rounded-lg",
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            )
                                        ],
                                        span=3,
                                    ),
                                ],
                            ),
                            create_grid(
                                3,
                                children=[
                                    create_grid_item(
                                        children=[
                                            html.Div(
                                                className="w-full h-auto px-6 py-12",
                                                children=[
                                                    create_card(
                                                        title="A Service Title",
                                                        description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sint, debitis! Rem, aspernatur nihil dolorum ducimus necessitatibus error, eos sunt quibusdam omnis officia accusantium praesentium ad hic soluta, pariatur possimus vitae! Voluptas asperiores quae quisquam qui obcaecati repellat, corrupti eveniet ducimus?",
                                                    ),
                                                ],
                                            )
                                        ]
                                    ),
                                    create_grid_item(
                                        children=[
                                            html.Div(
                                                className="w-full h-auto px-6 py-12",
                                                children=[
                                                    create_card(
                                                        title="A Second Title",
                                                        description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sint, debitis! Rem, aspernatur nihil dolorum ducimus necessitatibus error, eos sunt quibusdam omnis officia accusantium praesentium ad hic soluta, pariatur possimus vitae! Voluptas asperiores quae quisquam qui obcaecati repellat, corrupti eveniet ducimus?",
                                                        link="",
                                                        link_text="",
                                                    ),
                                                ],
                                            )
                                        ]
                                    ),
                                    create_grid_item(
                                        children=[
                                            html.Div(
                                                className="w-full h-auto px-6 py-12",
                                                children=[
                                                    create_card(
                                                        title="A Third Title",
                                                        description="Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sint, debitis! Rem, aspernatur nihil dolorum ducimus necessitatibus error, eos sunt quibusdam omnis officia accusantium praesentium ad hic soluta, pariatur possimus vitae! Voluptas asperiores quae quisquam qui obcaecati repellat, corrupti eveniet ducimus?",
                                                        link="",
                                                        link_text="",
                                                    ),
                                                ],
                                            )
                                        ]
                                    ),
                                ],
                            ),
                        ],
                        className="flex flex-col w-full mt-2 gap-4",
                    ),
                ],
            )
        ]
    )
    return layout
