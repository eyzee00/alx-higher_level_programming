#!/usr/bin/python3
"""Module: adds a row (object) named `Louisiana`to states"""

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

    newrow = State(name="Louisiana")
    session.add(newrow)
    session.commit()
    print(newrow.id)
