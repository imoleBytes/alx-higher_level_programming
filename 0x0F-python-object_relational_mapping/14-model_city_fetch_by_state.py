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
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(f"""mysql+mysqldb://{username}:{password}
                            @localhost:3306/{db}""")

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    instances = session.query(City).order_by(City.id)

    for i in instances:
        state_id = i.state_id
        obj = session.query(State).filter(State.id == state_id).first()
        word = f"{obj.name}: ({i.id}) {i.name}"
        print(word)


if __name__ == "__main__":
    main()
