#!/usr/bin/python3
"""All states via SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Wrong input")

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state is not None:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
