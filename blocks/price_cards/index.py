
# Import dominate
from dominate.util import raw
from dominate.tags import div, small, h3, h4, p, button


def main(data):

    # Import blockable modules
    from blockable import load_css

    # Create div and add css
    HTML = div(_class="grid-container")
    HTML += raw(load_css("blocks/price_cards/stylesheet.css"))
    card_grid = HTML.add(div(_class="price-grid"))

    for card in data["cards"]:
        # Create top level divs
        card_div = card_grid.add(div(_class="card text-center mx-auto my-3"))
        card_header = card_div.add(div(_class="card-header"))
        card_body = card_div.add(div(_class="card-body"))

        card_header += h3(card["label"], _class="h4 my-0")

        card_body += h4(card["price"], small("/mo", _class="muted-text"), _class="h2")
        card_body += p(raw(card["description"].replace("\n", "<br>")), _class="fake-list")
        card_body += button("Contact Us", _class="price-button", href="#contact")

    return HTML
