#!/usr/bin/python3
"""This modules contins main"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    objs = \
        session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for obj in objs:
        print(obj.id, obj.name, sep=": ")


if __name__ == "__main__":
    main()
