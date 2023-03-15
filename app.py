import dash
import dash_bootstrap_components as dbc

# Toggle the themes at [dbc.themes.LUX]
# The full list of available themes is:
# CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE,
# SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI.
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

external_scripts = ["https://cdn.tailwindcss.com"]

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.LUX],
    external_scripts=external_scripts,
)
