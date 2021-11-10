import asyncio
from contextlib import contextmanager
from datetime import datetime, timezone
from functools import wraps
from typing import Optional, TypeVar

from aiohttp import web
from prometheus_client import (
    CollectorRegistry,
    Counter,
    Histogram,
    Info,
    generate_latest,
)

from . import __version__
from .exceptions import BadRequestError, TooManyRequestsError, UnexpectedError
from .schemas import Event, StreamingResponse

__all__ = (
    'registry',
    'run_metrics_server',
    'create_app',
    'get_metrics',
    'collect_streaming_metrics',
    'collect_client_metrics',
)

T = TypeVar('T')

info = Info('tinvest_version', 'Tinvest')
info.info({'version': __version__})

registry = CollectorRegistry()

streaming_latency = Histogram(
    'tinvest_streaming_latency_seconds',
    'Streaming latency',
    ['event'],
    registry=registry,
)
streaming_latencies = {e: streaming_latency.labels(e.value) for e in Event}

http_requests_count = Counter(
    'tinvest_requests_total',
    'HTTP Requests',
    ['method', 'endpoint', 'status'],
    registry=registry,
)

STATUS_OK = 'ok'
STATUS_BAD_REQUEST_ERROR = 'bad_request_error'
STATUS_TOO_MANY_REQUESTS_ERROR = 'too_many_requests_error'
STATUS_UNEXPECTED_ERROR = 'unexpected_error'


def streaming_observe(event: StreamingResponse) -> None:
    streaming_latencies[event.event].observe(
        (datetime.utcnow().replace(tzinfo=timezone.utc) - event.time).total_seconds()
    )


@contextmanager
def _request_metrics_ctx(method: str, path: str):
    try:
        yield
    except BadRequestError:
        http_requests_count.labels(method, path, STATUS_BAD_REQUEST_ERROR).inc()
        raise
    except TooManyRequestsError:
        http_requests_count.labels(method, path, STATUS_TOO_MANY_REQUESTS_ERROR).inc()
        raise
    except UnexpectedError:
        http_requests_count.labels(method, path, STATUS_UNEXPECTED_ERROR).inc()
        raise
    else:
        http_requests_count.labels(method, path, STATUS_OK).inc()


def collect_client_metrics(client: T) -> T:
    # pylint:disable=protected-access
    original_request = client._request  # type:ignore

    async def request_wrapper(method: str, path: str, *args, **kwargs):
        with _request_metrics_ctx(method, path):
            return await original_request(method, path, *args, **kwargs)

    def sync_request_wrapper(method: str, path: str, *args, **kwargs):
        with _request_metrics_ctx(method, path):
            return original_request(method, path, *args, **kwargs)

    if asyncio.iscoroutinefunction(original_request):
        wraps(client._request)(request_wrapper)  # type:ignore
        client._request = request_wrapper  # type:ignore
    else:
        wraps(client._request)(sync_request_wrapper)  # type:ignore
        client._request = sync_request_wrapper  # type:ignore

    return client


def collect_streaming_metrics(streaming: T) -> T:
    # pylint:disable=protected-access
    original_events = streaming._get_events  # type:ignore

    async def streaming_events_wrapper():
        async for event in original_events():
            streaming_observe(event)
            yield event

    streaming._get_events = streaming_events_wrapper  # type:ignore
    return streaming


async def get_metrics(
    request: web.Request,  # pylint:disable=unused-argument
) -> web.Response:
    return web.Response(text=generate_latest(registry=registry).decode())


def create_app() -> web.Application:
    app = web.Application()
    app.router.add_get('/metrics', get_metrics)
    return app


async def run_metrics_server(
    host: Optional[str] = None, port: Optional[int] = None, app_factory=None
) -> web.AppRunner:
    if not app_factory:
        app_factory = create_app
    app = app_factory()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, host, port)
    await site.start()
    return runner
