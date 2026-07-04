from sqlalchemy import create_async_engine

from app.core.config import settings

engine = create_async_engine(settings.database_url, echo=settings.debug)
