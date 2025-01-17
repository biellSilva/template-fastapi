from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    add_routes(app)

    return app


def add_routes(app: FastAPI) -> None: ...
