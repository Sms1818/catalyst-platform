from app.app import create_app
from app.core.logging import setup_logging

setup_logging()


app = create_app()
