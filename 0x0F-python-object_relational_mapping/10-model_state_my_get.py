#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":

    path = "mysql+mysqldb://{}:{}@localhost/{}". \
        format(sys.argv[1], sys.argv[2], sys.argv[3])

    args = sys.argv[4].split(';')
    state_name = args[0].strip('"\'')

    engine = create_engine(path)
    Session = sessionmaker(bind=engine)
    session = Session()

    flag = 0
    for s in session.query(State):
        if s.name == state_name:
            print("{}".format(s.id))
            flag = 1
            break
    if flag == 0:
        print("Not found")
