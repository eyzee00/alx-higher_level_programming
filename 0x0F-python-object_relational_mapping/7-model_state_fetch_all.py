#!/usr/bin/python3
"""
Module: lists all states rows using sqlalchemy
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@\
            localhost/{}".format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for row in session.query(State).order_by(State.id):
        print("{}: {}".format(row.id, row.name))