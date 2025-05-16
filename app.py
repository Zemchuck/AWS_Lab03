from fastapi import FastAPI
from artifacts.inference import Inference

app = FastAPI()
inference = Inference("artifacts")


@app.get("/health")
async def health():
    return 200


@app.get("/")
async def home():
    return {"info": "Go to /docs endpoint"}


@app.post("/predict")
async def predict(text: str):
    return {"sentiment": inference.predict(text)}
