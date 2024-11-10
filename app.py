from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping/", response_class=JSONResponse)
def index():
    return {"message": "pong"}
