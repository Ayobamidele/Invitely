from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.sql import func
from api.db.db_model import Base
import hashlib
from sqlalchemy.event import listens_for



class Invitation(Base):
    __tablename_ = "Invitation"
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    created-at = Column(DateTime, default=func.now())