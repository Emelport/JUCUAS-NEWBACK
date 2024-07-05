from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *

# MODELO DE REPRESENTANTES
class Representative(Base):
    __tablename__ = 'representative'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="representative_user")
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(String(50))
    origin_university_id = Column(Integer, ForeignKey('university.id'), nullable=True)
    origin_university = relationship("University", foreign_keys=[origin_university_id])
    origin_organizational_unit_id = Column(Integer, ForeignKey('organizational_unit.id'), nullable=True)
    origin_organizational_unit = relationship("OrganizationalUnit", foreign_keys=[origin_organizational_unit_id])
    email = Column(String(50))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Representative(first_name='{self.first_name}', last_name='{self.last_name}')>"
