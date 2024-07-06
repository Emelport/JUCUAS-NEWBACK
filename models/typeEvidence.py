from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *
from db.base import Base


# MODELO DE TIPO DE EVIDENCIA
class TypeEvidence(Base):
    __tablename__ = 'type_evidence'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    type = Column(Enum('PDF', 'URL'))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)
    is_optional = Column(Boolean, default=False)

    def __repr__(self):
        return f"<TypeEvidence(name='{self.name}', type='{self.type}')>"

