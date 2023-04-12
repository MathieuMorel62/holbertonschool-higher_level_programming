#!/usr/bin/python3
"""
    Script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City


if __name__ == '__main__':
    # Get MySQL credentials and database name
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, database), pool_pre_ping=True)

    # Create tables in database
    Base.metadata.create_all(engine)

    # Create session to interact with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all State and City objects
    query = session.query(State).order_by(State.id).all()

    # Print results
    for state in query:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
