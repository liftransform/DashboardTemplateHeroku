from dash import html


def create_grid(col=3, children=[]):
    grid = html.Div(
        children=children,
        className=f"grid grid-cols-{col} gap-4 w-full",
    )

    return grid


def create_grid_item(children=[], span=1):
    grid_item = html.Div(
        children=children,
        className=f"bg-white rounded-lg p-2 border border-gray-200 col-span-{span} overflow-hidden",
    )

    return grid_item
