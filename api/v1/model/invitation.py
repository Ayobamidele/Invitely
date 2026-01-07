from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.sql import func
from db.base_model import Base
import hashlib
from sqlalchemy.event import listens_for



class Invitation(Base):
    __tablename_ = "Invitation"
    ID = Column(Integer, primary_key=True)
    Email = Column(String, nullable=False)
    Created = Column(DateTime, default=func.now())