from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


POSTGRES_PATH = "postgresql://ubuntu:ubuntu@127.0.0.1:5432"
postgres_engine = create_engine(
    POSTGRES_PATH,
    echo = False
)
PostgresSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=postgres_engine
)
Base = declarative_base()


def get_db():
    db = PostgresSessionLocal()
    try:
        yield db
    finally:
        db.close()
