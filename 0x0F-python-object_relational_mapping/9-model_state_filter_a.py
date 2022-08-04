#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    path = "mysql+mysqldb://{}:{}@localhost/{}". \
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(path)
    Session = sessionmaker(bind=engine)
    session = Session()
    for s in session.query(State).order_by(State.id). \
            filter(State.name.contains('a')):
        if s is None:
            print("Nothing")
        else:
            print("{}: {}".format(s.id, s.name))
