from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):
    pass


charity_crud = CRUDCharityProject(CharityProject)
