from flask import Flask
from loguru import logger
from sqlalchemy import create_engine

from reservas.configuration import persistence

user = persistence["user"]
host = persistence["host"]
port = persistence["port"]
vendor = persistence["vendor"]
driver = persistence["driver"]
database = persistence["database"]
passphrase = persistence["passphrase"]

application = Flask(__name__, "/reservas/static")

logger.debug("creating connection pool")
engine = create_engine(f"{vendor}+{driver}://{user}:{passphrase}@{host}/{database}", pool_recycle=3600, echo=True)
