import uvicorn
from fastapi import FastAPI
from loguru import logger

from fastapi_app.routers import router as main_router
from fastapi_app.tools.logs import configure_logger, get_uvicorn_log_config

app = FastAPI()


def main():
    configure_logger()
    logger.info("Starting...")

    app.include_router(main_router)

    uvicorn.run("fastapi_app.__main__:app", log_config=get_uvicorn_log_config())


if __name__ == "__main__":
    main()
