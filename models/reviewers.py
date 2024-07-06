from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from models.choices import *
from sqlalchemy.orm import relationship
from db.base import Base

# MODELO DE REVISORES
class Reviewer(Base):
    __tablename__ = 'reviewer'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="reviewer_user")
    first_name = Column(String(50))
    last_name = Column(String(50))
    user_name = Column(String(50))
    region = Column(Enum('N', 'CN', 'C', 'S'), nullable=True)
    global_reviewer = Column(Boolean, default=False)
    origin_university_id = Column(Integer, ForeignKey('university.id'), nullable=True)
    origin_university = relationship("University", foreign_keys=[origin_university_id])
    origin_highschool_id = Column(Integer, ForeignKey('university.id'), nullable=True)
    origin_highschool = relationship("University", foreign_keys=[origin_highschool_id], backref="origin_highschool")
    origin_organizational_unit_id = Column(Integer, ForeignKey('organizational_unit.id'), nullable=True)
    origin_organizational_unit = relationship("OrganizationalUnit", foreign_keys=[origin_organizational_unit_id])
    reviewer_permission = Column(String(10))
    email = Column(String(50))
    is_active = Column(Boolean, default=True)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Reviewer(first_name='{self.first_name}', last_name='{self.last_name}')>"

