#!/usr/bin/python3
"""
    Prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create engine to connect to database
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(user, passwd, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create session to interact with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for state with matching name
    query = session.query(State).filter(State.name == state_name)

    # Print state ID if found, else print "Not found"
    state = query.first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
