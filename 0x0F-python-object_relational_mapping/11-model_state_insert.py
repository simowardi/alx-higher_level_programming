#!/usr/bin/python3
"""
This script adds the State object
`Louisiana` to the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Establishing a connection to the database
    and adding a state object.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    # Creating a State object for Louisiana and adding it to the session
    lou_state = State(name='Louisiana')
    session.add(lou_state)
    session.commit()

    # Printing the id of the newly added State object
    print('{0}'.format(lou_state.id))

    # Closing the session
    session.close()
