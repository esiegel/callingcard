# Numbers we can speeddial.
# Dictionary from extension to person.
# ZERO is a reserved extension for dialing any number
SPEEDDIAL = {
    1: {"name": "Alice",
        "number": "+15555555551"},
    2: {"name": "Bob",
        "number": "+15555555552"},
    3: {"name": "Chris",
        "number": "+15555555553"},
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
