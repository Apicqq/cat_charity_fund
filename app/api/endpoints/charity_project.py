from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import check_has_investment
from app.core.db import get_async_session
from app.crud.charity_project import charity_crud
from app.schemas.charity_project import CharityProjectDB, CharityProjectCreate
from app.core.user import current_superuser

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
    """Superusers only."""
    return await charity_crud.post(project, session)


@router.delete(
    "/{project_id}",
    response_model=CharityProjectDB,
    dependencies=[Depends(current_superuser)])
async def delete_project(
        project_id: int,
        session: AsyncSession = Depends(get_async_session)
) -> CharityProjectDB:
    """Superusers only."""
    project = await check_has_investment(project_id, session)
    return await charity_crud.delete(project, session)


@router.patch("/{project_id}")
async def update_project():
    """Superusers only."""
    pass
