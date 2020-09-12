from functools import wraps

from flask import request, abort

from isDoorOpen.config.settings import settings
from hmac import compare_digest


def check_access_token(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = str(request.headers.get(settings.ACCESS_TOKEN_KEY, "none"))
        if settings.ENABLE_ACCESS_TOKEN_CHECK:
            if not compare_digest(token, settings.ACCESS_TOKEN_VALUE):
                return abort(401)
        return func(*args, **kwargs)

    return wrapper
