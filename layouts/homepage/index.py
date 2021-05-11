
# Import dominate
from dominate.tags import link, div, meta
import dominate


def main(data):
    # Import blocks and assets
    from blockable import blocks, assets

    font_link = "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap"

    # Start document and add css
    HTML = dominate.document()
    with HTML.head:
        link(href=assets("assets/css/stylesheet.css"), rel="stylesheet")
        link(href=font_link, rel="stylesheet")
        meta(charset="utf-8")



    # Add cover
    HTML += blocks.cover(data["cover"])

    # Create container and add blocks
    container = HTML.add(div(_class="container mx-auto py-3"))
    container += div(blocks.about(data["about"]), _class="py-3")
    container += div(blocks.key_points(data["key_points"]), _class="py-3")

    # Return html
    return HTML
