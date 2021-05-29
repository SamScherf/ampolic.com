
# Import modules
import dominate
from dominate.tags import link, meta
from dominate.util import raw


def main(data):

    from blockable import load_css
    font_link = "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap"

    HTML = dominate.document(title=data["title"])
    with HTML.head:
        raw(load_css("assets/css/stylesheet.css"))
        link(href=font_link, rel="stylesheet")
        meta(charset="utf-8")
        meta(name="viewport", content="width=device-width, user-scalable=no")

    return HTML
