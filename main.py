import json
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse, PlainTextResponse
from pydantic import BaseModel
from typing import List
from datetime import datetime
import base64

app = FastAPI()

#Q1
@app.get("/ping")
def ping():
    return Response(content="pong", media_type="text/plain", status_code=200);

#Q2
@app.get("/home", response_class=HTMLResponse)
async def home():
    return "<h1>Welcome home!</h1>"

#Q3
@app.get("/{full_path:path}")
def catch_all(full_path: str):
    with open("not_found.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return Response(content=html_content, status_code=200, media_type="text/html")



# Mémoire vive pour stocker les posts
posts_memory = []

# Modèle de données pour un post
class Post(BaseModel):
    author: str
    title: str
    content: str
    creation_datetime: datetime

# Q4
@app.post("/posts", status_code=201)
def create_posts(new_posts: List[Post]):
    posts_memory.extend(new_posts)
    return posts_memory

# Q5
@app.get("/posts")
def get_posts():
    return posts_memory

# Q6
@app.put("/posts")
def upsert_posts(updated_posts: List[Post]):
    global posts_memory
    updated_dict = {post.title: post for post in updated_posts}

    new_memory = []
    for post in posts_memory:
        if post.title in updated_dict:
            new_memory.append(updated_dict.pop(post.title))
        else:
            new_memory.append(post)

    new_memory.extend(updated_dict.values())

    posts_memory = new_memory
    return posts_memory