from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware  # Import the CORS middleware
from model.model import predict_sentiment
from database import store_prediction_in_db
from pydantic import BaseModel
from datetime import datetime
import os 
from dotenv import load_dotenv  # Import the dotenv module



app = FastAPI()

# Load environment variables from .env file
load_dotenv()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the origin of your frontend application
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Disable automatic handling of favicon.ico
app.mount("/favicon.ico", StaticFiles(directory=None), name="favicon")

# Setup basic authentication
security = HTTPBasic()

app.mount("/static", StaticFiles(directory="./static"), name="static")
templates = Jinja2Templates(directory="./templates")

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    prediction: str


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = os.getenv("USERNAME")  # Replace with your actual username variable
    correct_password = os.getenv("PASSWORD") # Replace with your actual password

    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )

@app.get("/")
def home(request: dict = Depends(authenticate_user)):
    return {"health_check": "OK"}

@app.post("/predict", response_model=PredictionOut)
async def predict(payload: TextIn, request: dict = Depends(authenticate_user)):
    try:
        pred = await predict_sentiment(payload.text)
        store_prediction_in_db(text=payload.text, prediction=pred)
        return {"prediction": pred}
    except Exception as e:
        print(f"Error in predict endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/dashboard")
async def dashboard(request: dict = Depends(authenticate_user)):
    predictions = [{"text": "example text", "prediction": "positive", "created_at": datetime.utcnow()}]  # Replace with actual data
    return templates.TemplateResponse("base.html", {"request": request, "predictions": predictions})

# Serve index.html as the main frontend
@app.get("/frontend", response_class=FileResponse)
def serve_frontend():
    return FileResponse("static/index.html")

@app.get("/styles.css", response_class=FileResponse)
def serve_styles():
    return FileResponse("static/styles.css")

@app.get("/script.js", response_class=FileResponse)
def serve_script():
    return FileResponse("static/script.js")
