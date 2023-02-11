from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
import models
from db import db
import uvicorn
from fastapi.templating import Jinja2Templates


app=FastAPI()
templates = Jinja2Templates(directory="templates")


def connect_db():
	try:
		yield db
	finally:
		db.close()



@app.get('/',response_class=HTMLResponse)
def index(request:Request):
	posts = db.query(models.Post.id,models.Post.text,models.Post.created_date).filter(models.Post.id<10).order_by(models.Post.created_date)
	return templates.TemplateResponse("basic.html",{'request':request,'posts':posts})

@app.get('/find')
def find():
	return FileResponse("templates/find.html")

@app.get('/delete')
def delete():
	return FileResponse("templates/delete.html")

if __name__=='__main__':
	uvicorn.run()