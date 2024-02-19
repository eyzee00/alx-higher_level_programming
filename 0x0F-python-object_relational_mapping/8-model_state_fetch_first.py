#!/usr/bin/python3
"""Module: prints the first row (object) in the table (class) State"""

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

    if session.query(State).order_by(State.id).first() is None:
        print("Nothing")
    else:
        first = session.query(State).order_by(State.id).first()
        print("{}: {}".format(first.id, first.name))
