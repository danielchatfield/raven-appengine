# raven-appengine

`raven-appengine` is an appengine compatible Transport for the raven-python client.

## Usage

Make sure your dsn uses one of the special protocols: `appengine+http` or `appengine+https`.
Make sure you have enabled `deferred` in your `app.yaml`
```yaml
builtins:
- deferred: on
```
Register the transport before setting up the `Sentry` instance.

```python
from raven_appengine import register_transport

register_transport()

# register sentry as usual
```
## Limitations

## License

Copyright (c) 2013 Daniel Chatfield. Licensed under the MIT license.