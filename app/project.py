from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, HTMLResponse
from models import Post
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
	posts = db.query(Post.id,Post.text,Post.created_date).order_by(Post.created_date)
	return templates.TemplateResponse("basic.html",{'request':request,'posts':posts})

@app.get('/find',response_class=HTMLResponse)
def find(request:Request):
	return templates.TemplateResponse("find.html",{'request':request})

@app.post('/findpost',response_class=HTMLResponse)
def findpost(request:Request,ids=Form()):
	posts = db.query(Post.id,Post.text,Post.created_date).filter(Post.id==ids).order_by(Post.created_date)
	return templates.TemplateResponse("find.html",{'request':request,'posts':posts})

@app.get('/delete',response_class=HTMLResponse)
def delete(request:Request):
	return templates.TemplateResponse("delete.html",{'request':request})

@app.post('/deletepost',response_class=HTMLResponse)
def deletepost(request:Request,ids=Form()):
	posts = db.query(Post).filter(Post.id==ids).first()
	print(posts)
	db.delete(posts)
	db.commit()
	return templates.TemplateResponse("delete.html",{'request':request})

if __name__=='__main__':
	uvicorn.run()