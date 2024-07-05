from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *

# MODELO DE PRESENTADORES
class Presenter(Base):
    __tablename__ = 'presenter'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="presenter_user", primaryjoin="Presenter.user_id == User.id")
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(String(50))
    gender = Column(Enum('M', 'H', 'O'), nullable=True)
    curp = Column(String(18))
    email = Column(String(50))
    phone = Column(String(10))
    academic_degree = Column(String(50))
    origin_university_id = Column(Integer, ForeignKey('university.id'), nullable=True)
    origin_university = relationship("University", foreign_keys=[origin_university_id])
    origin_organizational_unit_id = Column(Integer, ForeignKey('organizational_unit.id'), nullable=True)
    origin_organizational_unit = relationship("OrganizationalUnit", foreign_keys=[origin_organizational_unit_id])
    if_belong_to_school = Column(Boolean, default=True)
    position_institution = Column(Enum('1', '2', '3', '4', '5'), default='1')
    birth_date = Column(DateTime)
    created_by_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    created_by = relationship("User", foreign_keys=[created_by_id])
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)
    # Relación con Activity como presentador principal
    activity_presenter = relationship("Activity", back_populates="presenter")
    # Relación con Activity como co-presentador
    co_presenter_activities = relationship("Activity", secondary='activity_co_presenter',back_populates="co_presenters")
    def __repr__(self):
        return f"<Presenter(first_name='{self.first_name}', last_name='{self.last_name}')>"

