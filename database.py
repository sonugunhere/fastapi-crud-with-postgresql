from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from starlette.config import Config

# Config will be read from environment variables and/or ".env" files.
config = Config(".env")
ENVIRONMENT = config("ENVIRONMENT")
POSTGRES_HOST = config("POSTGRES_HOST")
POSTGRES_PORT = config("POSTGRES_PORT")
POSTGRES_USER = config("POSTGRES_USER")
POSTGRES_PASS = config("POSTGRES_PASS")
POSTGRES_DB = config("POSTGRES_DB")
DB_TYPE = config("DB_TYPE")

SQLALCHEMY_DATABASE_URL = f"{DB_TYPE}://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


