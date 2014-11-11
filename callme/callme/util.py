from flask import request, Response
from textwrap import dedent
from functools import wraps


def get_twiml_params(f):
    """gets the twiml parameters from the JSON post body, or the GET params"""

    @wraps(f)
    def decorated(*args, **kwargs):
        if request.method == "GET":
            twiml_params = request.args
        elif request.method == "POST":
            twiml_params = request.json if isinstance(request.json, dict) else {}
        else:
            twiml_params = {}

        return f(twiml_params, *args, **kwargs)

    return decorated


def produces_xml(f):
    """converts response txt to XML response object"""

    @wraps(f)
    def decorated(*args, **kwargs):
        xml = f(*args, **kwargs)
        return Response(dedent(xml), mimetype="text/xml")

    return decorated
