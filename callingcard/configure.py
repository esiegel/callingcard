from logging import basicConfig, getLogger, DEBUG
from logging.config import dictConfig
from json import loads
from os import environ 

from flask import request

from callingcard import defaults
from callingcard.controllers import create_routes


def configure_app(app, debug=False, testing=False):
    """
    Configure the application.

    Allows the application to be configured for interactive debugging or unit testing.

    If debug is enabled, `app.run()` will reload on source changes (assuming application
    code is installed in "editable" mode). If testing is enabled, the collaborators
    defined below may be modified to use mocks. Both settings change how uncaught
    exceptions are handled, either by logging to the console (debug) or propagating to the
    test client (testing).
    """

    app.debug = debug
    app.testing = testing

    _configure_from_defaults(app)
    _configure_from_environment_file(app)
    _configure_from_environment(app)
    _configure_stream_reading(app)
    _configure_logging(app)

    # Configure other collaborators (or mocks) here

    # Hook up controllers
    create_routes(app)


def _configure_from_defaults(app):
    """
    Load configuration defaults from defaults.py in this package.
    """
    app.config.from_object(defaults)


def _configure_from_environment_file(app):
    """
    Load configuration from a file specified as the value of
    the CALLINGCARD_SETTINGS environment variable.

    Don't complain if the variable is unset.
    """
    app.config.from_envvar("CALLINGCARD_SETTINGS", silent=True)


def _configure_from_environment(app):
    """
    Load configuration from environment variables.
    Tries to convert values based on the type specified
    in the default values.  For non simple types it is
    assumed that JSON was used for serialization.

    This is useful for deployments that only allow changing config
    via environment variables, and disallow uploading configuration
    that is not bundled with source, ie Heroku.
    """
    names = [name for name in dir(defaults)
             if name in environ and not name.startswith('__')]

    for name in names:
        _type = type(defaults.__dict__[name])
        raw_value = environ[name]

        if _type in [str, int, float]:
            # simple type
            value = _type(raw_value)
        else:
            # complex type
            value = loads(raw_value)
            if type(value) != _type:
                raise ValueError("Configuration type mismatch {}: {} != {}"
                                 .format(name, type(value).__name__, _type.__name__))

        app.config.__setattr__(name, value)


def _configure_stream_reading(app):
    """
    Ensure that nginx and uwsgi place nicely together.

    Under some error conditions, uwsgi will simply close its socket, causing clients
    to hang waiting for a response. See NS-281.
    """
    if app.config.get('FORCE_READ_REQUESTS'):
        @app.after_request
        def read_request(response):
            request.stream.read()
            return response


def _configure_logging(app):
    """
    Configure logging.
    """
    if app.testing or app.debug:
        basicConfig(level=DEBUG)
    else:
        dictConfig(app.config.get("LOGGING"))
        configured_logger = getLogger("callingcard")

        # ensure that Flask's logger uses configured handlers
        for handler in configured_logger.handlers:
            app.logger.addHandler(handler)

        app.logger.debug("Initialized logging")

