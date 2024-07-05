from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from db.base import Base
from models.choices import *
from sqlalchemy.orm import relationship


# MODELO DE UNIDADES ORGANIZACIONALES
class OrganizationalUnit(Base):
    __tablename__ = 'organizational_unit'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    acronym = Column(String(10))
    key_code = Column(String(10))
    region = Column(Enum('N', 'CN', 'C', 'S'), nullable=True)
    municipality = Column(String(150))
    locality = Column(String(150))
    email = Column(String(150))
    phone = Column(String(10))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<OrganizationalUnit(name='{self.name}')>"
