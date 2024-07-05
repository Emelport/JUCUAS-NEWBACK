from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *

# MODELO DE ACTIVIDAD
class Activity(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    description = Column(String(500))
    numbers_expected_attendees = Column(Integer)
    numbers_total_attendees = Column(Integer)
    modality = Column(Enum('V', 'P'))
    edition_id = Column(Integer, ForeignKey('deadline.id'))
    date_activity = Column(DateTime)
    educational_level_to_is_directed = Column(Enum('PCO', 'PREESC', 'PRIM', 'SEC', 'MDSUP', 'SUP'))
    type_of_public = Column(Enum('INT', 'EXT'))
    area_knowledge = Column(Enum('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'))
    presenter_id = Column(Integer, ForeignKey('presenter.id'))
    presenter = relationship("Presenter", back_populates="activity_presenter")
    co_presenters = relationship("Presenter", secondary='activity_co_presenter',back_populates="co_presenter_activities")
    type_id = Column(Integer, ForeignKey('type_activity.id'))
    type = relationship("TypeActivity")
    created_by_id = Column(Integer, ForeignKey('user.id'))
    created_by = relationship("User", foreign_keys=[created_by_id])
    certificate_file = Column(String(255))
    activity_status = Column(Enum('DUE', 'INC', 'REJECT', 'OK'))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)
    related_evidences = relationship('Evidence', back_populates='activity')


    def __repr__(self):
        return f"<Activity(name='{self.name}', date_activity='{self.date_activity}')>"