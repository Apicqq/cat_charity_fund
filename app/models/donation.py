from sqlalchemy import Column, Text, Integer, ForeignKey

from app.core.db import Base
from app.models.base import GenericFields


class Donation(Base, GenericFields):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text, nullable=True)
