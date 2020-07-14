"""
The asgi__ middleware for tracing all requests to an ASGI-compliant application.

To configure tracing manually::

    from ddtrace.contrib.asgi import TraceMiddleware

    async def app(scope, receive, send):
        assert scope["type"] == "http"
        headers = [[b"content-type", b"text/plain"]]
        await send({"type": "http.response.start", "status": 200, "headers": headers})
        await send({"type": "http.response.body", "body": b"Hello, world!"})

    app = TraceMiddleware(app)

Then use ddtrace-run when serving your application. For example, if serving with Uvicorn::

    ddtrace-run uvicorn app:app


Configuration
~~~~~~~~~~~~~

.. py:data:: ddtrace.config.asgi['distributed_tracing_enabled']

   Whether to use distributed tracing headers from requests received by your Asgi app.

   Default: ``True``

.. py:data:: ddtrace.config.asgi['analytics_enabled']

   Whether to analyze spans for Asgi in App Analytics.

   Can also be enabled with the ``DD_ASGI_ANALYTICS_ENABLED`` environment variable.

   Default: ``None``

.. py:data:: ddtrace.config.asgi['service_name']

   The service name reported for your ASGI app.

   Can also be configured via the ``DD_SERVICE`` environment variable.

   Default: ``'asgi'``

.. __: https://asgi.readthedocs.io/
"""

from ...utils.importlib import require_modules


required_modules = []

with require_modules(required_modules) as missing_modules:
    if not missing_modules:
        from .middleware import TraceMiddleware

        __all__ = ["TraceMiddleware"]
