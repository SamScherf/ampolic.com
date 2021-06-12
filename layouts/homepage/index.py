
# Import dominate
from dominate.tags import div


def main(data):
    # Import blocks and assets
    from blockable import blocks

    # Start document and open
    HTML = blocks.seo(data["seo"])
    with HTML:
        # Add cover
        div(blocks.cover(data["cover"]), _id="cover")

        # Create container and add blocks
        with div(_class="container mx-auto py-3", _id="content"):
            div(blocks.about(data["about"]), _class="py-3", _id="about")
            div(blocks.key_points(data["key_points"]), _class="py-3", _id="key_points")
            div(blocks.price_cards(data["price_cards"]), _class="py-3", _id="pricing")

        # Add contact form
        div(blocks.contact(data["contact"]), _id="contact")

    # Return html
    return HTML
