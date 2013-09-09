# raven-appengine

`raven-appengine` is an appengine compatible Transport for the raven-python client.

## Usage

1. Make sure your dsn uses one of the special protocols: `appengine+http` or `appengine+https`.
2. Enable `deferred` in your `app.yaml`

```yaml
builtins:
- deferred: on
```
3. Define the `sentry` queue

```
queue:
- name: sentry
  rate: 5/s
```
4. Register the transport before setting up the `Sentry` instance.

```python
from raven_appengine import register_transport

register_transport()

# register sentry as usual
```
## Limitations

Always calls the success callback, even if it fails. This is not a very big issue as appengine automatically retries failed attempts.

## License

Copyright (c) 2013 Daniel Chatfield. Licensed under the MIT license.