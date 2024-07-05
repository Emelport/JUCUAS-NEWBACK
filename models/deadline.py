from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *


# MODELO DE FECHAS LÍMITE
class Deadline(Base):
    __tablename__ = 'deadline'

    id = Column(Integer, primary_key=True)
    name_edition = Column(String(150))
    date_edition = Column(String(4))
    date_to_upload_activities = Column(Date)
    date_to_upload_evidence = Column(Date)
    date_to_validate_evidence = Column(Date)
    date_edition_start = Column(Date)
    end_date_of_the_edition = Column(Date)
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)
    file = Column(Text)
    file_name = Column(String(150))

    def __repr__(self):
        return f"<Deadline(name_edition='{self.name_edition}', date_edition='{self.date_edition}')>"
