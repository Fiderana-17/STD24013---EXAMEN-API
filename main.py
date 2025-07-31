import json

from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()

@app.get("/ping")
def ping():
    return Response(content="pong", media_type="text/plain", status_code=200);
