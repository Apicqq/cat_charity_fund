from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def get_all_projects():
    pass


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
