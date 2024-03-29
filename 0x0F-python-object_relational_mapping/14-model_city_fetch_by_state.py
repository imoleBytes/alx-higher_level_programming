#!/usr/bin/python3
"""
Write a Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""
import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """Starts here """
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f"""mysql+mysqldb://{username}:
                            {password}@localhost:3306/{db}""")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in (session.query(State.name, City.id, City.name)
                     .filter(State.id == City.state_id)):
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])


if __name__ == "__main__":
    main()
