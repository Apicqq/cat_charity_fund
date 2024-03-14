from sqlalchemy import Column, String, Text

from app.core.db import Base
from app.models.base import GenericFields
from app.services.constants import DBConstants as Dc


class CharityProject(Base, GenericFields):
    name = Column(
        String(Dc.CHARITY_PROJECT_NAME_DEFAULT), unique=True, nullable=False
    )
    description = Column(Text, nullable=False)
