#!/usr/bin/python3
"""Module: prints the rows in states with a name matching
the given argument
"""

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

    flag = False
    for state in session.query(State):
        if state.name == argv[4]:
            print("{}".format(state.id))
            flag = True
            break
    if not flag:
        print("Not found")
