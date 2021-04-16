
from dominate.tags import *
import dominate

def main(data):

    HTML = div(_class="custom-cover cover-image")
    
    mask = HTML.add(div(_class="mask"))

    text_row = mask.add(div(_class="mt-auto mx-auto"))

    carrot_row = mask.add(div(_class="mt-auto mx-auto c_link"))

    return HTML.render()
