

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    'textAlign': 'center',
    "top": 62.5,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0.5rem 1rem",
    #   "background-color": "#f8f9fa",  # cambiar color!!,
    'textAlign': 'center',
}

SIDEBAR_HIDEN = {
    "position": "fixed",
    "top": 62.5,
    "left": "-100rem",
    "bottom": 0,
    "width": "20rem",
    "height": "100%",
    "z-index": 1,
    "overflow-x": "hidden",
    "transition": "all 0.5s",
    "padding": "0rem 0rem",
    #    "background-color": "#f8f9fa",
    'textAlign': 'center',
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    #    "background-color": "#f8f9fa",
}

CONTENT_STYLE1 = {
    "transition": "margin-left .5s",
    "margin-left": "2rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    #    "background-color": "#f8f9fa",
}

DATE_PICKER_STYLE = {
    "position": "sticky",
    "top": 0

}

CARD_STYLE = {
    "margin-top": "2em",
    "padding": " 1.5em 0.5em 0.5em",
    "border-radius": "2em",
    "text-align": "center",
    "box-shadow": "0 5px 10px rgba(0, 0, 0, 0.2)"
}

CARD_IMG_STYLE = {
    "width": "65%",
    "border-radius": "50%",
    "margin": "0 auto",
    "box-shadow": "0 0 10px rgba(0, 0, 0, 0.2)"
}

CARD_TITLE = {
    "font-weight": "700",
    "font-size": "1.5em"
}
CARD_BUTTON = {
   "border-radius": "5em",
  "background-color": "teal",
  "color": "#ffffff",
  "padding": "0.5em 1.5em"
}