#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    comp = sys.argv[4]
    query = session.query(State).where(State.name == comp).first()

    if query:
        print("{}".format(query.id))
    else:
        print("Not found")

    session.close()
