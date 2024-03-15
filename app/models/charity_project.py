from sqlalchemy import Column, String, Text

from app.models.base import GenericFields
from app.core.constants import DBConstants as Db


class CharityProject(GenericFields):
    name = Column(
        String(Db.CHARITY_PROJECT_NAME_DEFAULT.value),
        unique=True,
        nullable=False,
    )
    description = Column(Text, nullable=False)

    def __repr__(self):
        return super().__repr__()
