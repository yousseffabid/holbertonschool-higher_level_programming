#!/usr/bin/python3
"""prints the first State object from the database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":

    path = "mysql+mysqldb://{}:{}@localhost/{}".\
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(path, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    s = session.query(State).order_by(State.id).first()
    if s is None:
        print("Nothing")
    else:
        print("{}: {}".format(s.id, s.name))
