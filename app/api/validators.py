from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.charity_project import charity_crud
from app.models import CharityProject
from app.schemas.charity_project import CharityProjectUpdate
from app.services.constants import ErrConstants as Err


async def check_name_is_busy(
        name: str,
        session: AsyncSession
) -> None:
    project_id = await charity_crud.get_project_id_by_name(name, session)
    if project_id is not None:
        raise HTTPException(
            HTTPStatus.BAD_REQUEST, Err.NAME_IS_BUSY
        )


async def check_has_investment(project_id: int,
                               session: AsyncSession) -> CharityProject:
    project: CharityProject = await charity_crud.get(project_id, session)
    if project is None:
        raise HTTPException(HTTPStatus.BAD_REQUEST, Err.NOT_FOUND)
    if project.invested_amount > 0:
        raise HTTPException(HTTPStatus.BAD_REQUEST,
                            Err.CANNOT_DELETE_PROJECT_WITH_INVESTMENTS)
    return project


async def check_eligible_for_patching(
        project_id,
        data_in: CharityProjectUpdate,
        session: AsyncSession
) -> CharityProject:
    project: CharityProject = await charity_crud.get(project_id, session)
    if project is None:
        raise HTTPException(HTTPStatus.NOT_FOUND,
                            Err.NOT_FOUND)
    if project.fully_invested:
        raise HTTPException(HTTPStatus.BAD_REQUEST,
                            Err.CANNOT_MODIFY_CLOSED_PROJECT)
    if (data_in.full_amount and
            data_in.full_amount < project.invested_amount):
        raise HTTPException(HTTPStatus.BAD_REQUEST,
                            Err.FULL_AMOUNT_LT_INVESTED_AMOUNT)
    if data_in.name != project.name:
        await check_name_is_busy(data_in.name, session)
    return project
