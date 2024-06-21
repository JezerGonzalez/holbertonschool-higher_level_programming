#!/usr/bin/python3
"""First state model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Start of class"""
    __tablename__ = 'states'
    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)
    cities = relationship("cities", back_populates="state")
