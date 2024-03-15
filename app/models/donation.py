from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models.base import InvestmentDateFields


class Donation(InvestmentDateFields):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text, nullable=True)

    def __repr__(self):
        return (f"{super().__repr__()},"
                f" user_id: {self.user_id}, comment: {self.comment}")
