from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from models.choices import *  # Base esta importada aqui


# MODELO DE EVIDENCIA
class Evidence(Base):
    __tablename__ = 'evidence'

    id = Column(Integer, primary_key=True)
    name = Column(String(300))
    observation = Column(String(1500))
    evidence_file = Column(String(255))
    evidence_status = Column(Enum('SEND', 'DUE', 'INC', 'REJECT', 'OK'))
    created_by_id = Column(Integer, ForeignKey('user.id'))
    created_by = relationship("User", foreign_keys=[created_by_id])
    status_changed_by_id = Column(Integer, ForeignKey('user.id'))
    status_changed_by = relationship("User", foreign_keys=[status_changed_by_id])
    type_evidence_id = Column(Integer, ForeignKey('type_evidence.id'))
    type_evidence = relationship("TypeEvidence")
    activity_id = Column(Integer, ForeignKey('activity.id'))
    activity = relationship("Activity", back_populates="related_evidences")

    def __repr__(self):
        return f"<Evidence(name='{self.name}', evidence_status='{self.evidence_status}')>"
