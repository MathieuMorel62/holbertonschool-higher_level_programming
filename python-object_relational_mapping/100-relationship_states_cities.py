#!/usr/bin/python3
"""
    Script that creates the State "California" with the City "San Francisco"
    from the database hbtn_0e_100_usa
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

    # Creation of a new city linked to the state and added to the database
    session.add(City(name="San Francisco", states=State(name="California")))
    session.commit()

    session.close()
