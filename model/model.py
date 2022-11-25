from random import randint
from pydantic import BaseModel

__version__ = "0.1.0"

happy = {"happy": "0.93", "angry": "0.20", "sad": "0.30", "aggressive": "0.50", "arrogant": "0.67"}
angry = {"happy": "0.45", "angry": "0.90", "sad": "0.30", "aggressive": "0.50", "arrogant": "0.67"}
sad = {"happy": "0.34", "angry": "0.20", "sad": "0.86", "aggressive": "0.50", "arrogant": "0.67"}
aggressive = {"happy": "0.56", "angry": "0.20", "sad": "0.30", "aggressive": "0.70", "arrogant": "0.67"}
arrogant = {"happy": "0.13", "angry": "0.20", "sad": "0.30", "aggressive": "0.50", "arrogant": "0.88"}
classes = [
    happy, angry, sad, aggressive, arrogant
]


class EmotionStatistics(BaseModel):
    happy: float
    angry: float
    sad: float
    aggressive: float
    arrogant: float

class PredictionOut(BaseModel):
    result: EmotionStatistics


def predict_pipeline(audio):
    print("Apply prediction process for audio:["+ audio.filename + "]")

#V1
    # value = randint(0,4)
    # print("val", value)
    # return classes[value]

#V2
    value = {
        "happy": randint(1,100)/100, 
        "angry": randint(1,100)/100, 
        "sad": randint(1,100)/100, 
        "aggressive": randint(1,100)/100, 
        "arrogant": randint(1,100)/100
    }
    print("val", value)
    return value