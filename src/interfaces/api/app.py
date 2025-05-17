from fastapi import FastAPI

from .routers import router
from src.infrastructure.config.settings import config


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Clean Surveys App",
        description="API REST que permite la creación y votación de encuestas",
        version=config.RELEASE_VERSION,
        contact={
            "name": "Brian",
            "email": "brianretamar0101@gmail.com",
        },
        license_info={
            "name": "MIT",
        },
        docs_url=None if config.ENVIRONMENT == "production" else "/docs",
        redoc_url=None if config.ENVIRONMENT == "production" else "/redoc",
    )
    init_routers(app_=app_)
    return app_


app = create_app()