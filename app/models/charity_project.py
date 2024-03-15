from sqlalchemy import Column, String, Text

from app.core.constants import DBConstants as Db
from app.models.base import CommonTableFields


class CharityProject(CommonTableFields):
    name = Column(
        String(Db.CHARITY_PROJECT_NAME_DEFAULT.value),
        unique=True,
        nullable=False,
    )
    description = Column(Text, nullable=False)

    def __repr__(self):
        return ', '.join((super().__repr__(), f"name: {self.name}",
                          f"description: {self.description}"))
