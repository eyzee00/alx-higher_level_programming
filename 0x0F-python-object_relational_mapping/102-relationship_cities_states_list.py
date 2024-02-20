#!/usr/bin/python3
"""Module: Lists all City objects from the database hbtn_0e_101_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for row in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(row.id, row.name, row.state.name))
