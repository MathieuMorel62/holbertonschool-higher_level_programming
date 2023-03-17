#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa"""

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

    # Update the name of the state with id=2 to New Mexico
    change_name_state = session.query(State).filter(State.id == 2).first()
    change_name_state.name = "New Mexico"
    session.commit()

    session.close()
