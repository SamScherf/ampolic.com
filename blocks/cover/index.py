
# Import dominate
import dominate
from dominate.tags import *
from dominate.util import raw

def main(data):
    
    # Import assets
    from blockable import assets

    # Create divs for cover and add css
    HTML = div()
    HTML += link(href=assets("blocks/cover/stylesheet.css"), rel="stylesheet")
    HTML += link(href=set_cover_image(data["image"]), rel="stylesheet")

    # Add cover with mask
    cover = HTML.add(div(_class="full-cover cover-image"))
    mask = cover.add(div(_class="dark-mask text-center"))

    # Add text
    text_row = mask.add(div(_class="mt-auto"))
    text_row += h1(data["header"])

    # Add down carrot
    carrot_row = mask.add(div(_class="mt-auto c_link"))
    carrot_row += raw(
    """
    <svg width="3em" height="3em" viewBox="0 0 16 16" class="bi bi-chevron-down" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
        <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"/>
    </svg>
    """
    )


    return HTML


def set_cover_image(image):
    from blockable import dynamic_css

    return dynamic_css("""
    .cover-image {
        background-image: url(%s)
    }
    """%image)
