from sqlalchemy import Table, Column, Integer, ForeignKey
from db.base import Base

activity_co_presenter = Table(
    'activity_co_presenter',
    Base.metadata,
    Column('activity_id', Integer, ForeignKey('activity.id')),
    Column('presenter_id', Integer, ForeignKey('presenter.id'))
)
