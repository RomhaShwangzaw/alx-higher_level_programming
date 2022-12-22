#!/usr/bin/python3
"""This script prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    State.cities = relationship(
            "City", order_by=City.id, back_populates="state")

    for s, c in session.query(State, City). \
            filter(State.id == City.state_id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
