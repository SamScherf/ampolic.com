
from dominate.tags import *
from dominate.util import raw

def main(data):
    from blockable import blocks
    
    HTML = div()

    HTML += h1("Welcome to the website")
    HTML += raw(blocks.cover({}))


    return HTML.render()
