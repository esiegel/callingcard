from callme.util import get_twiml_params, produces_xml


def create_routes(app):

    @app.route("/")
    def index():
        return "<h1>CallMe International</h1>"

    @app.route("/connect", methods=["GET", "POST"])
    @produces_xml
    @get_twiml_params
    def connect(twiml_params):
        return """<?xml version="1.0" encoding="UTF-8"?>
                  <Response>
                     <Gather action="/dial" timeout="30" numDigits="1">
                        <Say voice="woman" language="en">
                           Type the extension.
                        </Say>
                     </Gather>
                     <Say>We didn't receive the extension to dial</Say>
                  </Response>"""

    @app.route("/dial", methods=["GET", "POST"])
    @produces_xml
    @get_twiml_params
    def dial(twiml_params):

        index = int(twiml_params.get('Digits', '0'))
        number = app.config.get('NUMBERS')[index]

        return """<?xml version="1.0" encoding="UTF-8"?>
                  <Response>
                     <Dial>
                        <Number>{}</Number>
                     </Dial>
                  </Response>""".format(number)
