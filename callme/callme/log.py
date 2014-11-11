from logging import Filter
import socket


class HostnameAddingFilter(Filter):
    '''logging.Filter subclass that adds hostname to the logging message.

      After adding this filter to a logger or handler, one may include
      %(hostname)s in a format string.

      N.B. Messages propagate through parent loggers' handlers, not
      through the parent loggers themselves, so adding a filter to a
      logger is only effective for messages initiated through that
      logger.
   '''
    def filter(self, record):
        if not hasattr(record, 'hostname'):
            record.hostname = socket.getfqdn()

        # always permit logging of the record
        return True
