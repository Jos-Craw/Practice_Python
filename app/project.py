from fastapi import FastAPI
from fastapi.responses import FileResponse
from sqlalchemy import create_engine
from models import Post
from sqlalchemy.orm import sessionmaker


app=FastAPI()
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1111@localhost:5432/practice'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

@app.get('/')
def index():
	posts = db.query(Post).all()
	return posts

@app.get('/find')
def find():
	return FileResponse("templates/find.html")

@app.get('/delete')
def delete():
	return FileResponse("templates/delete.html")