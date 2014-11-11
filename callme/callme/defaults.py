# Numbers that can be redirected to.
NUMBERS = [
    "+15555555551",
    "+15555555552",
    "+15555555553",
    "+15555555554",
    "+15555555555",
    "+15555555556",
    "+15555555557",
    "+15555555558",
    "+15555555559",
]

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
