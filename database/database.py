from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///pets.db', connect_args={'check_same_thread': False})
Base = declarative_base()

Session_Declaration = sessionmaker(bind=engine)
session = Session_Declaration()

def create_db():
    Base.metadata.create_all(engine)