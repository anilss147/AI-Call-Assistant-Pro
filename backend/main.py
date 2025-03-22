from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "AI Call Assistant API is running!"}

@app.get("/docs")
def docs_redirect():
    return {"docs_url": "/redoc"}
