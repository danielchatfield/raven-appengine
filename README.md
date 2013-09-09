# raven-appengine

`raven-appengine` is an appengine optimised Transport for the `raven-python` client. It supports asynchronous sending of messages using Google's `deferred` library.

## Usage

* Make sure your dsn uses one of the special protocols: `appengine+http` or `appengine+https`.
* Enable `deferred` in your `app.yaml`

```yaml
builtins:
- deferred: on
```
* Define the `sentry` queue

```
queue:
- name: sentry
  rate: 5/s
```
* Register the transport before setting up the `Sentry` instance.

```python
from raven_appengine import register_transport

register_transport()

# register sentry as usual
```
## Limitations

Always calls the success callback, even if it fails. This is not a very big issue as appengine automatically retries failed attempts. Failed attempts still raise an exception that is logged to the appengine logger so it doesn't fail silently.

## License

Copyright (c) 2013 Daniel Chatfield. Licensed under the MIT license.