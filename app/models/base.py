from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime

from app.core.base import Base
from app.services.constants import DBConstants as Db


class GenericFields(Base):
    __abstract__ = True

    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=Db.INVESTED_AMOUNT_DEFAULT)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)
