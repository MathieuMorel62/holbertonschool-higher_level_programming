#!/usr/bin/python3
"""Module containing the City class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
import MySQLdb

Base = declarative_base()


class City(Base):
    """Class representing the cities table"""
    __tablename__ = 'cities'

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
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host='localhost',
        port=3306
    )
