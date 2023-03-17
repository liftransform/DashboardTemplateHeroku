from dash import html


def create_grid(col=3, children=[]):
    grid = html.Div(
        children=children,
        className=f"grid grid-cols-{col} gap-4 w-full",
    )

    return grid


def create_grid_item(children=[]):
    grid_item = html.Div(
        children=children,
        className="bg-white rounded-lg p-4 border border-gray-200",
    )

    return grid_item
