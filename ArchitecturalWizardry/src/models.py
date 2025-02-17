# src/models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class HubSpotField(Base):
    __tablename__ = 'hubspot_fields'
    id = Column(Integer, primary_key=True)
    field_name = Column(String(100), unique=True, nullable=False)
    field_type = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)

class UpsoEmailCadence(Base):
    __tablename__ = 'upso_email_cadences'
    id = Column(Integer, primary_key=True)
    cadence_name = Column(String(100), unique=True, nullable=False)
    timing = Column(String(50))  # e.g., 'daily', 'weekly'
    template_id = Column(Integer)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


# Setup the database connection
engine = create_engine('sqlite:///configurations.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
