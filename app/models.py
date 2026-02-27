from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    skills = Column(String, nullable=False)
    experience = Column(String, nullable=False)
    prediction = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    