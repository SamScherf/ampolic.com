# Import dominate
from dominate.tags import div, img, h3, p
from dominate.util import raw


def main(data):

    # Import css loader
    from blockable import load_css

    # Create div
    HTML = div(_class="grid")
    with HTML:
        # Add css
        HTML += raw(load_css("blocks/key_points/stylesheet.css"))

        # Loop though points
        for point in data["key_points"]:
            # Point div
            with div(_class="flex"):
                # Image div
                with div(_class="image-div py-3"):
                    img(src=point["icon"], width="70px", height="70px")

                # Text div
                with div(_class="text-div py-3"):
                    h3(point["title"])
                    p(point["description"])

    return HTML
