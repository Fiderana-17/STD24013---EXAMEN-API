import json

from fastapi import FastAPI
from starlette.responses import Response
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

