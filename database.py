
import os

from sqlalchemy import URL, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password=os.environ["DB_PASSWORD"],
    host="localhost",
    port=5432,
    database="inventory_db",
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
