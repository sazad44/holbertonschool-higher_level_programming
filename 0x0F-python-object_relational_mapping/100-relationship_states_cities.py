#!/usr/bin/python3
"""Py script to create State with City from database"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state = State(name="California")
    state.cities = [City(name="San Francisco")]
    session.add(state)
    session.commit()
    session.close()
