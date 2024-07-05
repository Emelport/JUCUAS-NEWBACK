from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *


# MODELO DE RESPONSABLE DE ACTIVIDAD
class ActivityManager(Base):
    __tablename__ = 'activity_manager'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="activity_manager_user")
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(Enum('M', 'H', 'O'), nullable=True)
    academic_degree = Column(Enum('L', 'M', 'D'), nullable=True)
    email = Column(String(50))
    birth_date = Column(DateTime)
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<ActivityManager(first_name='{self.first_name}', last_name='{self.last_name}')>"
