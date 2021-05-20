
# Import dominate
from dominate.util import raw
from dominate.tags import div, h2, form, _input, textarea


def main(data):

    # Import blockable modules
    from blockable import load_css

    # Create div and add css
    HTML = div(_class="dark-background text-center white-text")
    HTML += raw(load_css("blocks/contact/stylesheet.css"))
    container_div = HTML.add(div(_class="py-5 container"))
    contact_div = container_div.add(div(_class="mx-auto contact-div"))

    contact_div += h2("Contact Us")
    form_div = contact_div.add(form(_class="form-grid"))

    names_div = form_div.add(div(_class="grid"))
    names_div += div(
            _input(placeholder="First Name", _type="text", _class="text-input my-2"),
            _class="form-row")

    names_div += div(
            _input(placeholder="Last Name", _type="text", _class="text-input my-2"),
            _class="form-row")

    form_div += div(
            _input(placeholder="Email", _type="text", _class="text-input my-2"),
            _class="form-row")

    form_div += div(
            textarea(placeholder="Message", _type="text", rows="6", _class="text-input my-2"),
            _class="form-row")

    form_div += div(
            _input(value="Submit", _type="submit", _class="my-2 submit-button"),
            _class="form-row")

    return HTML
