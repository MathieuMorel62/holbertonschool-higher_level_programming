#!/usr/bin/python3
"""
    Script that deletes all State objects with a name containing the letter 'a'
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

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create session to interact with database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to delete all State objects containing 'a'
    delete_state = session.query(State).filter(State.name.like('%a%')).all()
    for state in delete_state:
        session.delete(state)
    session.commit()

    session.close()
