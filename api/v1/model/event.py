from enum import StrEnum
from sqlalchemy import Column, Float, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.sql import func
import hashlib
from db.base_model import Base
from sqlalchemy.event import listens_for


class Event(Base):
    __tablename__  = 'events'
    ID = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False) 
    DateTime = Column(DateTime, nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    guest_count = Column(Integer, nullable=True)
attendee_type = Column(StrEnum(Attendee_type), nullable=True)  # type: ignore