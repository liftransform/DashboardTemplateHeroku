import dash
import dash_bootstrap_components as dbc

# Toggle the themes at [dbc.themes.LUX]
# The full list of available themes is:
# CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE,
# SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI.
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

external_scripts = ["https://cdn.tailwindcss.com", "./assets/js/tailwind.js"]

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        "https://fonts.gstatic.com",
        "https://fonts.googleapis.com",
        "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&display=swap",
    ],
    external_scripts=external_scripts,
)


# <link rel="preconnect" href="https://fonts.googleapis.com">
# <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
# <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700;800;900&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
