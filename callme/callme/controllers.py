from callme.util import get_twiml_params, get_digits_entered, produces_xml
from flask import render_template


def create_routes(app):

    speeddial = app.config.get('SPEEDDIAL')

    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/connect", methods=["GET", "POST"])
    @produces_xml
    @get_twiml_params
    def connect(twiml_params):
        return render_template('connect.xml', speeddial=speeddial, timeout=15)

    @app.route("/switchboard", methods=["GET", "POST"])
    @produces_xml
    @get_twiml_params
    @get_digits_entered
    def switchboard(twiml_params, ext):
        if ext == 0:
            return render_template('freedial.xml', timeout=30)

        person = speeddial.get(ext, {})

        if not person:
            return render_template('invalid_extension.xml', ext=ext)

        return render_template('dial.xml', person=person)

    @app.route("/freedial", methods=["GET", "POST"])
    @produces_xml
    @get_twiml_params
    @get_digits_entered
    def freedial(twiml_params, number):
        person = {"name": "unknown", "number": number}
        return render_template('dial.xml', person=person)
