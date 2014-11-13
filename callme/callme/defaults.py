# Numbers we can speeddial.
# Dictionary from extension to person.
# ZERO is a reserved extension for dialing any number
SPEEDDIAL = {
    1: {"name": "Alice",
        "number": "+15555555551"},
    2: {"name": "Bob",
        "number": "+15555555552"},
    3: {"name": "Carl",
        "number": "+15555555553"},
    4: {"name": "Denise",
        "number": "+15555555554"},
    5: {"name": "Everret",
        "number": "+15555555555"},
    6: {"name": "Francis",
        "number": "+15555555556"},
    7: {"name": "Goodwin",
        "number": "+15555555557"},
    8: {"name": "Helga",
        "number": "+15555555558"},
    9: {"name": "Irwin",
        "number": "+15555555559"},
}

# Fully read every request to ensure the nginx and uwsgi play nice
FORCE_READ_REQUESTS = True

# Default logging configuration
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(hostname)s | %(asctime)s | %(levelname)s | %(name)s | %(message)s"
        }
    },
    "filters": {
        "add_hostname": {
            "()": "callme.log.HostnameAddingFilter"
        }
    },
    "handlers": {
        "file_handler": {
            "class": "logging.handlers.WatchedFileHandler",
            "formatter": "simple",
            "filename": "/var/log/callme/callme.log",
            "filters": ["add_hostname"]
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["file_handler"]
    },
}
