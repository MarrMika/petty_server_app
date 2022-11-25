from fastapi import FastAPI, UploadFile
from model.model import predict_pipeline
from model.model import __version__ as model_version
from model.model import PredictionOut


app = FastAPI()
        

@app.get("/api")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/api/predict", response_model=PredictionOut)
def predict(audio: UploadFile):
    result = predict_pipeline(audio)
    return {"result": result}