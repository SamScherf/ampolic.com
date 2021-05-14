
# Import modules
from dominate.tags import div, h2, p


def main(data):

    # Create div
    HTML = div(_class="text-center")

    # Add header and sub header
    HTML += h2(data["header"])
    HTML += p(data["sub_header"])

    return HTML
