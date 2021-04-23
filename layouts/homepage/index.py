
# Import dominate
from dominate.tags import *
from dominate.util import raw

def main(data):
    # Import blocks and assets
    from blockable import blocks, assets
   
    # Start document and add css
    HTML = html()
    HTML += link(href=assets("assets/css/stylesheet.css"), rel="stylesheet")
    HTML += link(href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap", rel="stylesheet")

    # Add cover
    HTML += blocks.cover(data["cover"])

    # Create container and add blocks
    container = HTML.add(div(_class="container mx-auto"))
    container += blocks.about(data["about"])

    
    # Return html
    return HTML
