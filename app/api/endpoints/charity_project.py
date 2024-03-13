from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_has_investment, check_name_is_busy, \
    check_eligible_for_patching
from app.core.db import get_async_session
from app.core.user import current_superuser
from app.crud.charity_project import charity_crud
from app.schemas.charity_project import CharityProjectDB, CharityProjectCreate, \
    CharityProjectUpdate

router = APIRouter()


@router.get("/", response_model=list[CharityProjectDB])
async def get_all_projects(
        session: AsyncSession = Depends(get_async_session),
):
    projects = await charity_crud.get_all(session)
    return projects


@router.post(
    "/",
    response_model=CharityProjectDB,
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)])
async def create_project(
        project: CharityProjectCreate,
        session: AsyncSession = Depends(get_async_session)
) -> CharityProjectDB:
    """Superusers only."""  # FIXME ADD ACTUAL DOCSTRING AND DESCRIPTION
    await check_name_is_busy(project.name, session)
    new_project = await charity_crud.post(project, session)
    return new_project


@router.delete(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)]
)
async def delete_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session)
) -> CharityProjectDB:
    """Superusers only."""  # FIXME ADD ACTUAL DOCSTRING AND DESCRIPTION
    project = await check_has_investment(project_id, session)
    return await charity_crud.delete(project, session)


@router.patch(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)],
    response_model_exclude_none=True)
async def update_project(
        project_id: int,
        obj_in: CharityProjectUpdate,
        session: AsyncSession = Depends(get_async_session)
):
    """Superusers only."""  # FIXME ADD ACTUAL DOCSTRING AND DESCRIPTION
    project = await check_eligible_for_patching(project_id, obj_in, session)
    project = await charity_crud.patch(project, obj_in, session)
    return project
