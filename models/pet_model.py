from email.policy import default
from sqlalchemy import Boolean, Column, Integer, String
from database.database import Base

class Pet(Base):
    __tablename__ = "Pets"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    pettype = Column(String)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}
