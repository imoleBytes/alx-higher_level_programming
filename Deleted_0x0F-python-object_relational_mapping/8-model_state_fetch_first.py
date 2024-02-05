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

    obj = session.query(State).first()
    if obj:
        print(obj.id, obj.name, sep=": ")
    else:
        print("Nothing")


if __name__ == "__main__":
    main()
