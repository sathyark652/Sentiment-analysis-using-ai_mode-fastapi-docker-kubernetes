import joblib
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/sentiment_model.joblib", "rb") as f:
    model = joblib.load(f)

classes = ["positive", "negative"]

async def predict_sentiment(text):
    text = text.lower()
    pred = model.predict([text])
    pred_class = str(pred[0])
    
    if pred_class in classes:
        return pred_class
    else:
        return "Unknown Class"



