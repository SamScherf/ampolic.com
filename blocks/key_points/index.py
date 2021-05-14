# Import dominate
from dominate.tags import div, img, h3, p
from dominate.util import raw


def main(data):

    # Import css loader
    from blockable import load_css

    # Create div and add css
    HTML = div(_class="grid")
    HTML += raw(load_css("blocks/key_points/stylesheet.css"))

    for point in data["key_points"]:
        point_div = HTML.add(div(_class="flex"))
        image_div = point_div.add(div(_class="image-div py-3"))
        text_div = point_div.add(div(_class="text-div py-3"))

        image_div += img(src=point["icon"], _class="key-icon")

        text_div += h3(point["title"])
        text_div += p(point["description"])

    return HTML
