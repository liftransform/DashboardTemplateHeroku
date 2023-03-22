from dash import html


def create_card(
    title="", description="", link="", link_text="learn more", variant="primary"
):
    primary_color = "#EBCABAb5"
    secondary_color = "#118467b5"

    card_color = primary_color if variant == "primary" else secondary_color

    card = html.Div(
        className="w-full h-full flex flex-col justify-center items-center relative",
        children=[
            html.H3(
                children=[f"{title}"],
                className="text-2xl font-bold text-gray-800 capitalize z-10",
            ),
            html.Div(
                className=f"h-72 w-72 bg-[{card_color}] opacity-60 rounded-full absolute -top-32 -left-32 z-0"
            ),
            html.Hr(className="w-1/2 border-gray-200 my-4"),
            html.P(
                children=[f"{description}"],
                className="text-gray-600 text-center text-xl z-10",
            ),
            html.A(
                children=[f"{link_text}"],
                href=f"{link}",
                className=f"text-[{secondary_color}] text-center z-10 underline mt-4",
            ),
        ],
    )

    return card
