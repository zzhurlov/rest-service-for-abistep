from fastapi import FastAPI

from app.core.constants import PROJECT_NAME, PROJECT_VERSION, DEBUG


def create_app():
    return FastAPI(
        title=PROJECT_NAME,
        version=PROJECT_VERSION,
        debug=DEBUG,
        docs_url="/api/docs",
    )
