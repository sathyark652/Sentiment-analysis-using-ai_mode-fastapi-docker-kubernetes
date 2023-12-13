# database.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Load database configuration from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", " ") #add deployed database url with image name: port 



# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a SQLAlchemy model for storing predictions in the database
Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(255), index=True)
    prediction = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

# Create the database tables
Base.metadata.create_all(bind=engine)

def store_prediction_in_db(text: str, prediction: str):
    db = SessionLocal()
    db_prediction = Prediction(text=text, prediction=prediction)
    db.add(db_prediction)
    db.commit()
    db.refresh(db_prediction)
    db.close()
