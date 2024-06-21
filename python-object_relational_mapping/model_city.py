#!/usr/bin/python3
"""First state model"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base
from sqlalchemy.orm import relationship

class City(Base):
    """Start of class"""
    __tablename__ = 'cities'
    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
