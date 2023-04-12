#!/usr/bin/python3
"""Module that lists all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Create engine to connect to database
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create session to interact with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all cities and their respective states ordered by city
    query = session.query(
        City, State).filter(State.id == City.state_id).order_by(City.id).all()

    # Print results
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
