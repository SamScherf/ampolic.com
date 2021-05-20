
# Import dominate
import dominate
from dominate.tags import link, div, meta
from dominate.util import raw


def main(data):
    # Import blocks and assets
    from blockable import blocks, load_css

    font_link = "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap"

    # Start document and add css
    HTML = dominate.document(title="Ampolic Digital Solutions")
    with HTML.head:
        raw(load_css("assets/css/stylesheet.css"))
        link(href=font_link, rel="stylesheet")
        meta(charset="utf-8")

    # Add cover
    HTML += blocks.cover(data["cover"])

    # Create container and add blocks
    container = HTML.add(div(_class="container mx-auto py-3", _id="content"))
    container += div(blocks.about(data["about"]), _class="py-3", _id="about")
    container += div(blocks.key_points(data["key_points"]), _class="py-3", _id="key_points")
    container += div(blocks.price_cards(data["price_cards"]), _class="py-3", _id="pricing")

    # Add contact form
    HTML += div(blocks.contact({}), _id="contact")

    # Return html
    return HTML
