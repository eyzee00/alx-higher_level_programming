#!/usr/bin/python3
"""Module defines a states class"""

from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines a States object (Table)"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
