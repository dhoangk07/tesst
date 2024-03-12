from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"hello":"success deploy to Hugging Face from local"}