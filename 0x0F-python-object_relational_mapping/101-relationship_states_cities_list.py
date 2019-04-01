#!/usr/bin/python3
"""Py script to list all objects and their corresponding children"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for sta in session.query(State).order_by(State.id):
        print("{}: {}".format(sta.id, sta.name))
        for cit in sta.cities:
            print("    {}: {}".format(cit.id, cit.name))
    session.close()
    engine.dispose()
