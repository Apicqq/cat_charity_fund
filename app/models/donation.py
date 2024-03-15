from sqlalchemy import Column, Text, Integer, ForeignKey

from app.models.base import CommonTableFields


class Donation(CommonTableFields):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text, nullable=True)

    def __repr__(self):
        return ", ".join((super().__repr__(), f"user_id: {self.user_id}",
                          f"comment: {self.comment}"))
