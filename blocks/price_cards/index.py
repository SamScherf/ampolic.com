from dominate.tags import div, img, link, h3, p
from blockable import assets


def main(data):

    # Create div and add css
    HTML = div(_class="grid-container")
    HTML += link(href=assets("blocks/price_cards/stylesheet.css"), rel="stylesheet")

    return HTML
