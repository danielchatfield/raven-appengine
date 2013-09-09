# -*- coding: utf-8 -*-
"""
    raven_appengine
    ~~~~~~~~~~~~~~~

    A raven transport that uses the appengine deferred library. This transport
    does not verify that the message was sent successfully.

    :copyright: (c) 2013 by Daniel Chatfield
"""
from libs import fix_path

from raven.transport import AsyncTransport, HTTPTransport

from google.appengine.api.taskqueue import UnknownQueueError

try:
    from google.appengine.ext import deferred
except:
    raise ImportError("AppEngineTransport requires the deferred "
                      "library. Enable it in the builtins section "
                      "of app.yaml.")

fix_path()

class AppEngineTransport(AsyncTransport, HTTPTransport):
    """
    This provides a transport that uses the appengine deferred library.

    This transport does not verify that the message was successful, although
    appengine provides automatic retrying.
    """
    scheme = ['appengine+http', 'appengine+https']

    def __init__(self, parsed_url):
        

        super(AppEngineTransport, self).__init__(parsed_url)

        # Remove the 'appengine+' from the protocol
        self._url = self._url.split('+', 1)[-1]

    def async_send(self, data, headers, success_cb, failure_cb):
        try:
            deferred.defer(self.send, data, headers, _queue="sentry")
        except UnknownQueueError:
            raise UnknownQueueError("The sentry queue must be defined in "
                                    "queue.yaml.")
        success_cb()

def register_transport():
    from raven import Client
    Client.register_scheme('appengine+http', AppEngineTransport)
