from dominate.tags import div, small, h2, h3, h4, p, a, button
from dominate.util import raw


def main(data):

    # Import blockable modules
    from blockable import load_css

    # Create div and add css
    with div(_class="grid-container") as HTML:
        raw(load_css("blocks/price_cards/stylesheet.css"))

        # Add section header
        with div(_class="py-3 text-center"):
            h2(data["header"])
            p(data["sub_header"])

        # Card grid
        with div(_class="price-grid"):

            # Create div for each card
            for card in data["cards"]:
                with div(_class="card text-center mx-auto my-3"):

                    # Card header
                    with div(_class="card-header"):
                        h3(card["label"], _class="h4 my-0")

                    # Card body
                    with div(_class="card-body"):
                        h4(card["price"], small("/mo", _class="muted-text"), _class="h2")
                        p(raw(card["description"].replace("\n", "<br>")), _class="fake-list")
                        a(button("Contact Us", _class="price-button"), href="#contact", _class="no_line")

    return HTML
