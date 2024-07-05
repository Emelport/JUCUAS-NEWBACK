from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *  # Base esta importada aqui

# TABLA DE RELACIÓN PARA ACTIVIDAD Y PRESENTADOR
class ActivityCoPresenter(Base):
    __tablename__ = 'activity_co_presenter'

    activity_id = Column(Integer, ForeignKey('activity.id'), primary_key=True)
    co_presenter_id = Column(Integer, ForeignKey('presenter.id'), primary_key=True)

