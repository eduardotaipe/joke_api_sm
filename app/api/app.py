from fastapi import FastAPI

from app.api.endpoints.joke import router as joke_router
from app.api.endpoints.mathematic import router as math_router
from app.api.open_api import get_custom_open_api
from app.core.config import get_settings
from app.db import init_db


SETTINGS = get_settings()


def init_app():
    app: FastAPI = FastAPI()
    app.include_router(joke_router, prefix=SETTINGS.API_V1_STR, tags=["Jokes"])
    app.include_router(math_router, prefix=SETTINGS.API_V1_STR, tags=["Maths"])
    app.openapi = get_custom_open_api(app)
    init_db()
    return app
