from sqlalchemy import Column, String, Text

from app.models.base import GenericFields
from app.services.constants import DBConstants as Db


class CharityProject(GenericFields):
    name = Column(
        String(Db.CHARITY_PROJECT_NAME_DEFAULT), unique=True, nullable=False
    )
    description = Column(Text, nullable=False)

    def __repr__(self):
        return f"Charity project #{self.id}: {self.name}"
