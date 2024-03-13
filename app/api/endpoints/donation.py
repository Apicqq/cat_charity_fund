from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_donations():
    pass


@router.post("/")
async def create_donation():
    pass


@router.get("/my")
async def get_own_donations():
    pass
