from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from models.choices import *
from db.base import Base


# MODELO DE UNIVERSIDADES
class University(Base):
    __tablename__ = 'university'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    acronym = Column(String(10))
    key_code = Column(String(10))
    type = Column(Enum('PREESC', 'PRIM', 'SEC', 'P', 'U'), nullable=True)
    region = Column(Enum('N', 'CN', 'C', 'S'), nullable=True)
    municipality = Column(String(150))
    locality = Column(String(150))
    email = Column(String(150))
    phone = Column(String(10))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<University(name='{self.name}')>"
