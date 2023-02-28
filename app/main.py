from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, HTMLResponse
from app.models import Post
from app.db import db
import uvicorn
from fastapi.templating import Jinja2Templates
import elasticsearch
from elasticsearch import Elasticsearch
import os


app=FastAPI()
templates = Jinja2Templates(directory="templates")


def connect_db():
	try:
		yield db
	finally:
		db.close()


def search(txt:str):
	result=Elasticsearch(os.getenv("ELASTIC")).search(index='practice',body={
		"size":20,
		"query": {
			"match":{
				"text":txt
			}
		}
	})
	res_id = [{"id_": item["_id"], "id": item["_source"]["id"]} for item in result["hits"]["hits"]]
	return res_id

@app.get('/',response_class=HTMLResponse)
def index(request:Request):
	return templates.TemplateResponse("basic.html",{'request':request})

@app.get('/find',response_class=HTMLResponse)
def find(request:Request):
	return templates.TemplateResponse("find.html",{'request':request})

@app.post('/findpost',response_class=HTMLResponse)
def findpost(request:Request,ids=Form()):
	id_list = [item["id"] for item in search(ids)]
	posts = db.query(Post).filter(Post.id.in_(id_list)).order_by(Post.created_date)
	return templates.TemplateResponse("find.html",{'request':request,'posts':posts})

@app.get('/delete',response_class=HTMLResponse)
def delete(request:Request):
	return templates.TemplateResponse("delete.html",{'request':request})

@app.post('/deletepost',response_class=HTMLResponse)
def deletepost(request:Request,ids=Form()):
	posts = db.query(Post).filter(Post.id==ids).first()
	if posts != None:
		db.delete(posts)
	db.commit()
	return templates.TemplateResponse("delete.html",{'request':request})
	