
# Import modules
from dominate.tags import div, h2, p


def main(data):

    # Create div
    with div(_class="text-center") as HTML:
        # Add header and sub header
        h2(data["header"])
        p(data["sub_header"])

    return HTML
