from fastapi import FastAPI

from app.core.constants import PROJECT_NAME, PROJECT_VERSION, DEBUG
from app.api.users import user_router


def create_app():
    app = FastAPI(
        title=PROJECT_NAME,
        version=PROJECT_VERSION,
        debug=DEBUG,
        docs_url="/api/docs",
    )
    app.include_router(user_router)

    return app
