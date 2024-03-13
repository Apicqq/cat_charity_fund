from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.charity_project import charity_crud
from app.schemas.charity_project import CharityProjectDB

router = APIRouter()


@router.get("/", response_model=list[CharityProjectDB])
async def get_all_projects(
        session: AsyncSession = Depends(get_async_session),
):
    projects = await charity_crud.get_all(session)
    return projects


@router.post("/")
async def create_project():
    """Superusers only."""
    pass


@router.delete("/{project_id}")
async def delete_project():
    """Superusers only."""
    pass


@router.patch("/{project_id}")
async def update_project():
    """Superusers only."""
    pass
