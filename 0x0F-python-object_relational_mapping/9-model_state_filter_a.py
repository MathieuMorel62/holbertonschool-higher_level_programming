#!/usr/bin/python3
"""lists all State objects that contain the letter 'a' from hbtn_0e_6_usa"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


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

    # Query for states with 'a' in their name, ordered by id
    qr = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    # Print all states
    for state in qr:
        print("{}: {}".format(state.id, state.name))

    session.close()
