from flask import Flask
from callme.configure import configure_app


def create_app(debug=False, testing=False):
    """
    Create the application.
    """
    app = Flask(__name__.split('.')[0])
    configure_app(app, debug=debug, testing=testing)
    return app
