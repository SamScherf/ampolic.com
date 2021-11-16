
# Import dominate
from dominate.tags import div, h1, a
from dominate.util import raw


def main(data):

    # Import modules
    from blockable import save_css, load_css

    # Create divs for cover and add css
    with div() as HTML:
        # Add css
        raw(load_css("blocks/cover/stylesheet.css"))
        raw(save_css(
            """
            .cover-image {
                background-image: url(%s)
            }
            """ % data["image"]))

        # Add cover and mask
        with div(_class="full-cover cover-image"):
            with div(_class="dark-mask text-center"):
                # Add text
                with div(_class="mt-auto"):
                    h1(data["header"])

                # Add down carrot
                with div(_class="mt-auto"):
                    a(raw(
                        """
                        <svg width="3em" height="3em" viewBox="0 0 16 16" class="bi bi-chevron-down" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"/>
                        </svg>
                        """
                        ),
                        href="#about",
                        _class="white")

    return HTML
