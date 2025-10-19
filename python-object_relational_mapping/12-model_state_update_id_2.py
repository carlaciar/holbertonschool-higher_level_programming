#!/usr/bin/python3
"""Changes the name of a State object with id = 2 to 'New Mexico'."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the state with id = 2
    state = session.query(State).filter_by(id=2).first()

    # If found, update its name
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
