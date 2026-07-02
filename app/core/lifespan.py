from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logger.info("Starting up the application...")
    # Perform startup tasks here
    yield
    logger.info("Shutting down the application...")
    # Perform shutdown tasks here
