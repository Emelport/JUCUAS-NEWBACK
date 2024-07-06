from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *
from db.base import Base


# Definición de la tabla de relación
type_activity_type_evidence = Table(
    'type_activity_type_evidence',  # Nombre de la tabla en la base de datos
    Base.metadata,  # Metadatos de la base de datos donde se define la tabla
    Column('type_activity_id', Integer, ForeignKey('type_activity.id')),  # Clave foránea a type_activity
    Column('type_evidence_id', Integer, ForeignKey('type_evidence.id'))  # Clave foránea a type_evidence
)


# MODELO DE TIPO DE ACTIVIDAD
class TypeActivity(Base):
    __tablename__ = 'type_activity'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    title = Column(String(800))
    max_copresenter = Column(String(100))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)
    type_evidence = relationship("TypeEvidence", secondary=type_activity_type_evidence)

    def __repr__(self):
        return f"<TypeActivity(name='{self.name}', title='{self.title}')>"
