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
        try:
            db.close()
        except Exception as e:
            print(e) # loop가 새로운 db를 주지않고 기존 db를 주고 있음 싱글턴의 영향일 수도 있고 아닐 수도 있다 디버깅 해야함
