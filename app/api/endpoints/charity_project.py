from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_has_investment,
    check_name_is_busy,
    check_eligible_for_patching,
)
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud import charity_crud, donation_crud
from app.models import CharityProject
from app.schemas.charity_project import (
    CharityProjectDB,
    CharityProjectCreate,
    CharityProjectUpdate,
)
from app.services.investments import do_run_investments

router = APIRouter()


@router.get("/", response_model=list[CharityProjectDB])
async def get_all_projects(
    session: AsyncSession = Depends(get_async_session),
) -> list[CharityProject]:
    """
    Retrieve all charity projects from the database. Available to everyone.

    :param session: The async session for the database.
     Defaults to get_async_session.
    :returns: list[CharityProject] - A list of charity projects
      retrieved from the database.
    """
    projects = await charity_crud.get_all(session)
    return projects


@router.post(
    "/",
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def create_project(
    project: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
) -> CharityProject:
    """
    Create a new charity project. Available only to superusers.

    :param project: Schema of the charity project to be created.
    :param session: The async session for the database.
     Defaults to get_async_session.
    :returns: CharityProject - The newly created charity project.
    """
    await check_name_is_busy(project.name, session)
    new_project = await charity_crud.post(project, session)
    await do_run_investments(new_project, donation_crud, session)
    return new_project


@router.delete(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
)
async def delete_project(
    project_id: int, session: AsyncSession = Depends(get_async_session)
) -> CharityProject:
    """
    Delete a charity project by it's id. Available only to superusers.

    :param project_id: ID of a project to be deleted.
    :param session: The async session for the database.
     Defaults to get_async_session.
    :returns: CharityProject - Deleted charity project.
    """
    project = await check_has_investment(project_id, session)
    return await charity_crud.delete(project, session)


@router.patch(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True,
)
async def update_project(
    project_id: int,
    obj_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
) -> CharityProject:
    """
    Update a charity project. Available only to superusers.

    :param project_id: ID of a project to be updated.
    :param obj_in: Data passed by the user for Project to be updated with.
    :param session: The async session for the database.
     Defaults to get_async_session.

    :returns: CharityProject - Updated charity project.
    """
    project = await check_eligible_for_patching(project_id, obj_in, session)
    project = await charity_crud.patch(project, obj_in, session)
    await do_run_investments(project, donation_crud, session)
    return project
