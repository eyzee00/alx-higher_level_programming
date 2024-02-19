#!/usr/bin/python3
"""
Module: changes the name of the object with an id of 2
to 'New Mexico'
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

    target = session.query(State).filter_by(id=2).first()
    target.name = "New Mexico"
    session.commit()
