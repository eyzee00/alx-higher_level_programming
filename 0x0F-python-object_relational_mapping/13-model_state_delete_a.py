#!/usr/bin/python3
"""
Module: deletes all the state rows (objects)
containing a in their name
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    session.commit()
