
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.extension import _rate_limit_exceeded_handler

def setup_rate_limiter(app):

    app.add_exception_handler(
        RateLimitExceeded,
        _rate_limit_exceeded_handler
    )
    app.add_middleware(SlowAPIMiddleware)

