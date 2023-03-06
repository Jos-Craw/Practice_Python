from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


#Создание сессии подключения сервиса к Postgres
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@postgres:5432/practice'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()