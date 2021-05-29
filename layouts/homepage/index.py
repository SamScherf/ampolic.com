
# Import dominate
from dominate.tags import div


def main(data):
    # Import blocks and assets
    from blockable import blocks

    # Start document and add css
    HTML = blocks.seo(data["seo"])

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
