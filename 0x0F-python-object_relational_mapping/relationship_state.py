#!/usr/bin/python3
"""Start link class to table in database"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'

    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        primary_key=True,
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    cities = relationship(
        "City",
        backref='states',
        cascade="all, delete-orphan"
    )
