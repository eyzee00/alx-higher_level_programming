#!/usr/bin/python3
"""Module: prints all state rows with names containing 'a'"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    joker = 'a'
    for state in session.query(State).order_by(State.id):
        if joker in state.name:
            print("{}: {}".format(state.id, state.name))
