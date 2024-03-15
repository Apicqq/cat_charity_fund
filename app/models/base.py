from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime, CheckConstraint

from app.core.base import Base
from app.services.constants import DBConstants as Db


class GenericFields(Base):
    __abstract__ = True

    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=Db.INVESTED_AMOUNT_DEFAULT.value)
    fully_invested = Column(Boolean, default=False)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)

    __table__args__ = (
        CheckConstraint(
            "full_amount > 0",
            name=Db.INVESTMENT_CONSTRAINT.value),
        CheckConstraint(
            "invested_amount <= full_amount",
            name=Db.INVESTMENT_LT_FUL_AMOUNT_CONSTRAINT.value
        )
    )

    def __repr__(self):
        return f"{self.__class__.__name__}, id={self.id}"
