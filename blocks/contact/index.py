"""
file: block/contact/index.py

This file implements a simple contact form
"""

# Import dominate
from dominate.util import raw
from dominate.tags import div, p, h2, form, _input, textarea, script


def main(data):
    """ get contact form html

    """

    # Import blockable modules
    from blockable import load_css, load_js

    # Create div and add css
    HTML = div(_class="dark-background text-center white-text")
    with HTML:
        raw(load_css("blocks/contact/stylesheet.css"))
        raw(load_js("blocks/contact/javascript.js"))
        raw(load_js("assets/js/minAjax.js"))
        script(src='https://hcaptcha.com/1/api.js', _async=True, defer=True)

        # Start container div
        with div(_class="py-5 container"):
            h2(data["header"])
            p(_id="form-response")

            # Create html form
            with form(_class="form-grid mx-auto contact-div", _id="form", onsubmit="submitForm(event)"):
                # Add first and last _id
                with div(_class="grid"):
                    # First name
                    with div(_class="form-row"):
                        _input(
                                placeholder="First Name",
                                _type="text",
                                _class="text-input my-2",
                                _id="first_name",
                                name="first_name",
                                required=True,
                                )
                    # Last name
                    with div(_class="form-row"):
                        _input(
                                placeholder="Last Name",
                                _type="text",
                                _class="text-input my-2",
                                _id="last_name",
                                name="last_name",
                                required=True,
                                )

                # Add email
                with div(_class="form-row"):
                    _input(
                            placeholder="Email",
                            _type="text",
                            _class="text-input my-2",
                            _id="email",
                            name="email",
                            required=True,
                            )

                # Add message
                with div(_class="form-row"):
                    textarea(
                            placeholder="Message",
                            _type="text",
                            rows="6",
                            _class="text-input my-2",
                            _id="message",
                            name="message",
                            required=True,
                            )

                # Add h-captcha
                with div(_class="form-row mx-auto py-2"):
                    div(_class="h-captcha", data_sitekey="d827d0bd-2dc5-4981-9784-b837691433b8")

                # Add submit button
                with div(_class="form-row"):
                    _input(
                            value="Submit",
                            _type="submit",
                            # _type="button",
                            # onclick="submitForm()",
                            _class="my-2 submit-button",
                            )

    return HTML
