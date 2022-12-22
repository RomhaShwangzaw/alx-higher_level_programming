#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the DB
"""

import sys
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for st in session.query(State).order_by(State.id).all():
        print("{}: {}".format(st.id, st.name))
        for city in st.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
