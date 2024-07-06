from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from models.choices import *
from db.base import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(150), unique=True)
    password = Column(String(60))
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(Enum(GenderEnum), default=GenderEnum.N, nullable=True)
    phone = Column(String(10), default="Asigna uno", nullable=True)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', phone='{self.phone}')>"


