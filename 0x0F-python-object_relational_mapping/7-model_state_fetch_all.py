#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    path_name = "mysql+mysqldb://{}:{}@localhost/{}". \
            format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(path_name)
    Session = sessionmaker(bind=engine)
    session = Session()

    for s in session.query(State).order_by(State.id):
        print("{}: {}".format(s.id, s.name))
