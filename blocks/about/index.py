
from dominate.tags import *
import dominate


def main(data):

    # Create div
    HTML = div(_class="text-center")

    # Add header and sub header
    HTML += h2(data["header"])
    HTML += p(data["sub_header"])

    return HTML

    



