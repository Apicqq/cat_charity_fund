from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_crud
from app.models import CharityProject


async def check_name_is_busy(
        name: str,
        session: AsyncSession
) -> None:
    project_id = await charity_crud.get_project_id_by_name(name, session)
    if project_id is not None:
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, "TO BE CHANGED LATER!"  # FIXME
        )


async def check_has_investment(project_id: int,
                               session: AsyncSession) -> CharityProject:
    project: CharityProject = await charity_crud.get(project_id, session)
    if project is None:
        raise HTTPException(HTTPStatus.BAD_REQUEST, "Not Found")
    if project.invested_amount > 0:
        raise HTTPException(HTTPStatus.BAD_REQUEST,
                            "TO BE CHANGED LATER!")  # FIXME
    return project
