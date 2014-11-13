"""
Run a development server.

Running a development server allows changes
to the application to be automatically reloaded.
"""
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

from callingcard.app import create_app


def main():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-a',
                        dest='interfaces',
                        action='store_const',
                        default={},
                        const=dict(host='0.0.0.0'),
                        help='Listen on all interfaces')
    parser.add_argument('-p',
                        dest='port',
                        type=int,
                        default=5555,
                        help='Listen port')
    args, extra = parser.parse_known_args()

    app = create_app(debug=True)

    app.run(port=args.port, **args.interfaces)
