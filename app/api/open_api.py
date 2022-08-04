from typing import Any, Callable, Dict

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.core.config import get_settings


SETTINGS = get_settings()


def get_custom_open_api(app: FastAPI) -> Callable[[], Dict[str, Any]]:
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=SETTINGS.PROJECT_NAME,
        version=SETTINGS.PROJECT_VERSION,
        description=SETTINGS.PROJECT_DESCRIPTION,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    def fn() -> Any:
        return app.openapi_schema

    return fn
