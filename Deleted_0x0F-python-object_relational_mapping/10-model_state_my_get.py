#!/usr/bin/python3
"""script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def main():
    """main function"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    objs = \
        session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(objs.id)
    except Exception:
        print("Not found")


if __name__ == "__main__":
    main()
