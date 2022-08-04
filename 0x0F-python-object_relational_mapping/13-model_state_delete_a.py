#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":

    path = "mysql+mysqldb://{}:{}@localhost/{}". \
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(path, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for s in session.query(State):
        if 'a' in State.name:
            session.delete(State)

    session.commit()
