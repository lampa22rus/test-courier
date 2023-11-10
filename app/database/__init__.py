from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

Base = declarative_base()

load_dotenv()

SQLALCHEMY_DATABASE_URL = 'postgresql://courier:courier@postgres/courier'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionScoped = scoped_session( SessionLocal)
def session_dependency():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()