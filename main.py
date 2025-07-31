import json
from fastapi import FastAPI,Response
from fastapi.responses import HTMLResponse



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
