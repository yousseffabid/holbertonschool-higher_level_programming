#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


if __name__ == "__main__":

    path = "mysql+mysqldb://{}:{}@localhost/{}". \
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(path, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(City, State) \
                        .filter(City.state_id == State.id) \
                        .order_by(City.id)

    for c, s in all_states:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
