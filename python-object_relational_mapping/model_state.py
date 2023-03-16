#!/usr/bin/python3
"""Start link class to table in database"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import MySQLdb

Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__= 'states'

    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        primary_key=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    connection = MySQLdb.connect(
    host='localhost',
    port=3306
    )