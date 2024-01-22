'''importing sqlalhemy, sys, and model_state'''
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

path = "mysql+mysqldb://{}:{}@localhost/{}"
engine = create_engine(path.format(argv[1], argv[2], argv[3]))

Session = sessionmaker(bind = engine)
session = Session()

states = session.query(State).order_by(State.id).first()

filter = session.query(State).filter(State.name.contains('a')).order_by(State.id).all()
for states in filter:
    print("{}: {}".format(states.id, states.name))

session.close()