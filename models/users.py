from sqlalchemy import Table, Column, Integer, String, Enum, Boolean, ForeignKey, DateTime, Date, Text
from models.choices import *
from db.base import Base
from sqlalchemy.orm import relationship

user_group_association = Table(
    'user_group_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('group_id', Integer, ForeignKey('group.id'))
)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(150), unique=True)
    password = Column(String(255))
    first_name = Column(String(50))
    last_name = Column(String(50))
    gender = Column(Enum(GenderEnum), default=GenderEnum.N, nullable=True)
    phone = Column(String(10), default="Asigna uno ", nullable=True)

    groups = relationship(
        'Group',
        secondary=user_group_association,
        back_populates='users'
    )

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', phone='{self.phone}')>"


class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    users = relationship(
        'User',
        secondary=user_group_association,
        back_populates='groups'
    )

    def __repr__(self):
        return f"<Group(name='{self.name}')>"
