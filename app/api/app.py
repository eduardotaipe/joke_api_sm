from fastapi import FastAPI

from app.api.endpoints.jokes import router as joke_router
from app.api.open_api import get_custom_open_api
from app.core.config import get_settings
from app.db import init_db


SETTINGS = get_settings()


def init_app():
    app: FastAPI = FastAPI()
    app.include_router(joke_router, prefix=SETTINGS.API_V1_STR, tags=["jokes"])
    app.openapi = get_custom_open_api(app)
    init_db()
    return app
