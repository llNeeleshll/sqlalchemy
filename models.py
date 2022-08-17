from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///pets.db', echo=True)
Base = declarative_base()

class Pet(Base):
    __tablename__ = "Pets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    pettype = Column(String)

    def __repr__(self) -> str:
        return f'The name of per it : {self.name} its age is {self.age} and is of type - {self.pettype}'

if __name__ == "__main__":
    Base.metadata.create_all(engine)