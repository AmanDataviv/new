from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:db_pswrd@pgdb:5432/mydatabase"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()