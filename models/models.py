from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Longitud especificada para VARCHAR
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255)) # °°°°°|CAMBIO, SE AGREGO PASSWORD
