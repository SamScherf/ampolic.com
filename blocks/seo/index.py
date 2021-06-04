
# Import modules
import dominate
from dominate.tags import link, meta
from dominate.util import raw


def main(data):

    from blockable import load_css, site_data

    # Get data
    settings = site_data("settings/meta")
    font_link = "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap"

    HTML = dominate.document(title=data["title"])
    with HTML.head:
        # Add css
        raw(load_css("assets/css/stylesheet.css"))
        link(href=font_link, rel="stylesheet")

        # Add favicon
        link(rel="icon", _type="image/icon type", href=settings["favicon"])

        # set general meta tags
        meta(charset="utf-8")
        meta(name="viewport", content="width=device-width, user-scalable=no")

    return HTML
