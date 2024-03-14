from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models.base import GenericFields


class Donation(GenericFields):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text, nullable=True)

    def __repr__(self):
        return super().__repr__()
