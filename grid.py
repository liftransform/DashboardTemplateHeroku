from dash import html

def create_grid(col=3, children=[]):
    grid = html.Div(
        children=children,
        className=f"grid grid-cols-{col} gap-4 w-full",
    )

    return grid
